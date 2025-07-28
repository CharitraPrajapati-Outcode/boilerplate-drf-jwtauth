#!/bin/bash

APP_NAME=$1
APPS_DIR="apps"
APP_PATH="$APPS_DIR/$APP_NAME"

if [ -z "$APP_NAME" ]; then
  echo "❌ Please provide an app name."
  echo "Usage: ./create_app.sh <app_name>"
  exit 1
fi

# Check for manage.py
if [ ! -f "manage.py" ]; then
  echo "❌ Error: manage.py not found. Run from Django project root."
  exit 1
fi

# Activate virtualenv if venv exists
if [ -d "venv" ]; then
  echo "🐍 Activating virtual environment..."
  source venv/bin/activate
fi

# Get Python command
PYTHON_CMD=$(command -v python || command -v python3)
if [ -z "$PYTHON_CMD" ]; then
  echo "❌ Python not found."
  exit 1
fi

# Create apps dir if missing
mkdir -p "$APPS_DIR"
touch "$APPS_DIR/__init__.py"

# Stop if app already exists
if [ -d "$APP_PATH" ]; then
  echo "⚠️ App '$APP_NAME' already exists at $APP_PATH"
  exit 1
fi

echo "🚀 Creating application..."

# ❗ Pre-create app directory
mkdir -p "$APP_PATH"

# Run Django startapp
$PYTHON_CMD manage.py startapp "$APP_NAME" "$APP_PATH"

echo "✅ Django app '$APP_NAME' created with default structure."

# Only proceed if files exist
if [ ! -f "$APP_PATH/views.py" ] || [ ! -f "$APP_PATH/models.py" ] || [ ! -f "$APP_PATH/tests.py" ]; then
  echo "❌ Error: Django default files missing. Aborting restructure."
  exit 1
fi

# Custom folders
mkdir -p "$APP_PATH/api/v1/serializers"
mkdir -p "$APP_PATH/api/v1/views"
mkdir -p "$APP_PATH/tests"
mkdir -p "$APP_PATH/models"

# Move original files to new structure
mv "$APP_PATH/views.py" "$APP_PATH/api/v1/views/views.py"
mv "$APP_PATH/models.py" "$APP_PATH/models/$(echo "$APP_NAME" | awk '{print tolower($0)}').py"
mv "$APP_PATH/tests.py" "$APP_PATH/tests/test_${APP_NAME}.py"

# __init__.py for Python packages
touch "$APP_PATH/api/__init__.py"
touch "$APP_PATH/api/v1/__init__.py"
touch "$APP_PATH/api/v1/serializers/__init__.py"
touch "$APP_PATH/api/v1/views/__init__.py"
touch "$APP_PATH/models/__init__.py"
touch "$APP_PATH/tests/__init__.py"

# urls.py
cat <<EOF > "$APP_PATH/api/v1/urls.py"
from django.urls import path

urlpatterns = [
    # path('', views.YourView.as_view(), name='your-view'),
]
EOF

echo "📁 Final structure ready at: $APP_PATH"
