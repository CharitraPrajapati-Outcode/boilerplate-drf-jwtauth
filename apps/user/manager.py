from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import ValidationError

from apps.common.constants import ADMIN


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')

        groups = extra_fields.get('groups')
        extra_fields.pop('groups')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        for group in groups:
            group.user_set.add(user)

        return user

    def create(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        try:
            groups = extra_fields.get('groups')
            if not groups:
                raise ValidationError('Group name is required')

            extra_fields.update({'groups': groups})
            return self._create_user(email, password, **extra_fields)
        except (ObjectDoesNotExist, ValidationError) as err:
            raise ValueError(err)

    def create_superuser(self, email, password, **extra_fields):
        group, _ = Group.objects.get_or_create(name=ADMIN)

        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.update({'groups': [group]})

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        return self._create_user(email, password, **extra_fields)
