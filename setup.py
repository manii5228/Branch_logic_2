#!/usr/bin/env python3
"""
BranchLogic Job Board - Setup Script
This script sets up the Flask application with all dependencies
"""

import os
import sys
import subprocess
import platform

def run_command(command, description):
    """Run a shell command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        if e.stdout:
            print(f"STDOUT: {e.stdout}")
        if e.stderr:
            print(f"STDERR: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required")
        print(f"Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} detected")
    return True

def create_virtual_environment():
    """Create a virtual environment"""
    if os.path.exists('venv'):
        print("✅ Virtual environment already exists")
        return True
    
    print("🔄 Creating virtual environment...")
    if run_command("python -m venv venv", "Creating virtual environment"):
        print("✅ Virtual environment created")
        return True
    return False

def activate_virtual_environment():
    """Activate virtual environment and install dependencies"""
    if platform.system() == "Windows":
        activate_script = "venv\\Scripts\\activate"
        pip_cmd = "venv\\Scripts\\pip"
    else:
        activate_script = "venv/bin/activate"
        pip_cmd = "venv/bin/pip"
    
    print("🔄 Installing dependencies...")
    
    # Upgrade pip
    if not run_command(f"{pip_cmd} install --upgrade pip", "Upgrading pip"):
        return False
    
    # Install requirements
    if not run_command(f"{pip_cmd} install -r requirements.txt", "Installing requirements"):
        return False
    
    print("✅ Dependencies installed successfully")
    return True

def setup_database():
    """Set up the database with sample data"""
    print("🔄 Setting up database...")
    
    # Create uploads directory
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
        print("📁 Created uploads directory")
    
    # Run database population script
    if platform.system() == "Windows":
        python_cmd = "venv\\Scripts\\python"
    else:
        python_cmd = "venv/bin/python"
    
    if run_command(f"{python_cmd} populate_db.py", "Setting up database"):
        print("✅ Database setup completed")
        return True
    return False

def main():
    """Main setup function"""
    print("🚀 BranchLogic Job Board Setup")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Create virtual environment
    if not create_virtual_environment():
        print("❌ Failed to create virtual environment")
        sys.exit(1)
    
    # Install dependencies
    if not activate_virtual_environment():
        print("❌ Failed to install dependencies")
        sys.exit(1)
    
    # Setup database
    if not setup_database():
        print("❌ Failed to setup database")
        sys.exit(1)
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Activate the virtual environment:")
    if platform.system() == "Windows":
        print("   venv\\Scripts\\activate")
    else:
        print("   source venv/bin/activate")
    print("2. Run the application:")
    print("   python run.py")
    print("3. Open your browser and go to: http://localhost:5000")
    print("\n🔑 Default login credentials:")
    print("   Job Seeker: jobseeker@example.com / password123")
    print("   Employer: employer@example.com / password123")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Setup interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)
