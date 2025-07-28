#!/bin/bash

# Usage: ./create_app.sh app_name

APP_NAME=$1
APPS_DIR="apps"

if [ -z "$APP_NAME" ]; then
  echo "❌ Please provide an app name."
  echo "Usage: ./create_app.sh <app_name>"
  exit 1
fi

# Check for manage.py in current directory
if [ ! -f "manage.py" ]; then
  echo "❌ Error: manage.py not found in current directory."
  echo "Please run this script from the root of your Django project."
  exit 1
fi

# Activate virtualenv if venv exists
if [ -d "venv" ]; then
  echo "🐍 Activating virtual environment..."
  source venv/bin/activate
fi

# Check for available Python interpreter
PYTHON_CMD=$(command -v python || command -v python3)
if [ -z "$PYTHON_CMD" ]; then
  echo "❌ Neither 'python' nor 'python3' found in PATH."
  exit 1
fi

# Create apps directory if it doesn't exist
if [ ! -d "$APPS_DIR" ]; then
  echo "📁 Creating $APPS_DIR directory..."
  mkdir "$APPS_DIR"
  touch "$APPS_DIR/__init__.py"
fi

# Create the app inside apps/
if [ -d "$APPS_DIR/$APP_NAME" ]; then
  echo "⚠️ App '$APP_NAME' already exists in $APPS_DIR/"
else
  echo "🚀 Creating Django app '$APP_NAME' inside $APPS_DIR/"
  mkdir -p "$APPS_DIR/$APP_NAME"
  $PYTHON_CMD manage.py startapp "$APP_NAME" "$APPS_DIR/$APP_NAME"
fi

echo "✅ Done. Your app is located at: $APPS_DIR/$APP_NAME/"
