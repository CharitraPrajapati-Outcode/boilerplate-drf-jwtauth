
# running application using gunicorn
grun:
	@echo "Running application with gunicorn..."
	gunicorn --bind 0.0.0.0:8000 config.wsgi --reload --workers 3 --timeout 120

# create app using bash/create_app.sh
create_app:
	@echo "Creating application..."
	bash bash/create_app.sh $(app_name)

# run migrations
migrate:
	@echo "Running migrations..."
	python manage.py migrate $(app_name) $(migration_name)

# make migrations
makemigrations:
	@echo "Making migrations..."
	python manage.py makemigrations
