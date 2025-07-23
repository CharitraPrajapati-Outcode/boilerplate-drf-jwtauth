import uuid

from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone
from django_currentuser.db.models import CurrentUserField

unicode_validator = UnicodeUsernameValidator()


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)


class SoftDeleteModel(models.Model):
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = SoftDeleteManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = '-updated_at',
        abstract = True


class AuditModel(models.Model):
    """
    Abstract model to add created_by and updated_by fields.
    """
    created_by = CurrentUserField(
        related_name="%(app_label)s_%(class)s_created",
        on_delete=models.SET_NULL,
        null=True,
        editable=False
    )

    updated_by = CurrentUserField(
        on_update=True,
        related_name="%(app_label)s_%(class)s_modified",
        on_delete=models.SET_NULL,
        null=True
    )

    class Meta:
        abstract = True


class CustomPrimaryKey(models.Model):
    id = models.UUIDField(max_length=150, primary_key=True, validators=[unicode_validator], default=uuid.uuid4,
                          editable=False)

    class Meta:
        abstract = True


class BaseModel(TimeStampModel, SoftDeleteModel, CustomPrimaryKey, AuditModel):
    class Meta:
        ordering = '-updated_at',
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.full_clean()
        return super().save(force_insert=False, force_update=False, using=None,
                            update_fields=None)

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super(BaseModel, self).delete()
