#!/usr/bin/env bash
set -e

if [ ! -f .env ]; then
  echo "ERROR: .env not found. Copy .env.example to .env and fill in your credentials."
  exit 1
fi

echo "Installing dependencies..."
pip install -r requirements.txt --quiet

echo "Starting server..."
python -m app.main