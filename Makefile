
# running application using gunicorn
grun:
	@echo "Running application with gunicorn..."
	gunicorn --bind 0.0.0.0:8000 config.wsgi --reload --workers 3 --timeout 120
