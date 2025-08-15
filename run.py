#!/usr/bin/env python3
"""
BranchLogic Job Board - Flask Application
A professional job board platform built with Flask and SQLAlchemy
"""

import os
import sys
from app import app, db

def main():
    """Main entry point for the application"""
    print("🚀 Starting BranchLogic Job Board...")
    
    # Ensure we're in the right directory
    if not os.path.exists('app.py'):
        print("❌ Error: app.py not found. Please run this script from the project root directory.")
        sys.exit(1)
    
    # Create uploads directory if it doesn't exist
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
        print("📁 Created uploads directory")
    
    # Initialize database
    with app.app_context():
        db.create_all()
        print("🗄️  Database initialized")
    
    print("✅ Application ready!")
    print("🌐 Open your browser and go to: http://localhost:5001")
    print("⏹️  Press Ctrl+C to stop the server")
    
    # Run the application
    app.run(debug=True, host='0.0.0.0', port=5001)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Server stopped. Goodbye!")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
