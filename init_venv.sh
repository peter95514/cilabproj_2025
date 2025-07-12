#!/bin/bash

VENV_DIR="venv"

echo "creating virtual environment..."
python3 -m venv $VENV_DIR

if [ ! -d "$VENV_DIR" ]; 
then
    echo "failed to create virtual environment"
    exit 1
fi 

echo "virtual environment created"

source $VENV_DIR/bin/activate

pip install --upgrade pip

if [ -f "requirements.txt" ]; then
    echo "Installing from requirements.txt..."
    pip install -r requirements.txt
else
    echo "⚠️ No requirements.txt found. Skipping installation."
fi

echo "Exporting updated requirements to requirements.txt..."
pip freeze > requirements.txt

deactivate

echo "Setup complete! Virtual environment is ready."
echo "To activate it later, run: source $VENV_DIR/bin/activate"


