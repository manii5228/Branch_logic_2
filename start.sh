#!/bin/bash

# BranchLogic Job Board - Startup Script

echo "🚀 Starting BranchLogic Job Board..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Please run setup.py first."
    exit 1
fi

# Activate virtual environment
echo "📦 Activating virtual environment..."
source venv/bin/activate

# Check if database exists
if [ ! -f "jobs.db" ]; then
    echo "🗄️  Database not found. Setting up database..."
    python populate_db.py
fi

# Create uploads directory if it doesn't exist
if [ ! -d "uploads" ]; then
    mkdir uploads
    echo "📁 Created uploads directory"
fi

# Start the application
echo "✅ Starting Flask application..."
echo "🌐 Open your browser and go to: http://localhost:5000"
echo "⏹️  Press Ctrl+C to stop the server"

python run.py
