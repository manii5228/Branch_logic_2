# BranchLogic Job Board

A professional job board platform built with Flask, SQLAlchemy, and modern web technologies. This application provides a complete solution for job seekers and employers to connect and manage job opportunities.

## ✨ Features

### 🎯 Job Seekers
- **Job Search & Discovery**: Advanced search with filters for location, category, job type, and remote work
- **Job Applications**: Easy application process with resume uploads and cover letters
- **Personal Dashboard**: Track applications, view status, and manage profile
- **Profile Management**: Complete professional profile with skills, experience, and portfolio links
- **Job Alerts**: Stay updated with new opportunities (coming soon)

### 🏢 Employers
- **Job Posting**: Create detailed job listings with requirements and benefits
- **Application Management**: Review and manage incoming applications
- **Company Dashboard**: Overview of posted jobs and application statistics
- **Candidate Search**: Browse and filter potential candidates (coming soon)
- **Analytics**: Track job performance and application metrics

### 🌐 General Features
- **Responsive Design**: Mobile-first approach with modern UI/UX
- **User Authentication**: Secure login/signup with role-based access
- **File Uploads**: Resume and document management
- **Search & Filters**: Advanced job search capabilities
- **Professional UI**: Clean, modern interface built with pure CSS

## 🛠️ Technology Stack

- **Backend**: Flask (Python web framework)
- **Database**: SQLAlchemy ORM with SQLite
- **Authentication**: Flask-Login for user sessions
- **Frontend**: HTML5, CSS3 (internal styles), Jinja2 templates
- **File Handling**: Werkzeug for secure file uploads
- **Security**: Password hashing, session management

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git (for cloning the repository)

## 🚀 Quick Start

### Option 1: Automated Setup (Recommended)

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd branchlogic-sample-0q-1
   ```

2. **Run the setup script**:
   ```bash
   python setup.py
   ```

3. **Start the application**:
   ```bash
   python run.py
   ```

4. **Open your browser** and go to `http://localhost:5001`

### Option 2: Manual Setup

1. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the database**:
   ```bash
   python populate_db.py
   ```

4. **Run the application**:
   ```bash
   python run.py
   ```

## 🔑 Default Login Credentials

### Job Seeker Account
- **Email**: `jobseeker@example.com`
- **Password**: `password123`

### Employer Account
- **Email**: `employer@example.com`
- **Password**: `password123`

## 📁 Project Structure

```
branchlogic-sample-0q-1/
├── app.py                 # Main Flask application
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── run.py                 # Application entry point
├── setup.py               # Automated setup script
├── start.sh               # Shell startup script
├── populate_db.py         # Database population script
├── templates/             # HTML templates
│   ├── base.html         # Base template
│   ├── index.html        # Homepage
│   ├── jobs.html         # Job listings
│   ├── job_detail.html   # Individual job view
│   ├── login.html        # Login page
│   ├── signup.html       # Registration page
│   ├── dashboard.html    # Job seeker dashboard
│   ├── employer_dashboard.html  # Employer dashboard
│   ├── post_job.html     # Job posting form
│   ├── apply_job.html    # Job application form
│   ├── profile.html      # User profile management
│   ├── 404.html          # 404 error page
│   └── 500.html          # 500 error page
├── uploads/               # File uploads directory
├── jobs.db                # SQLite database
└── README.md              # This file
```

## 🗄️ Database Models

### User
- Basic info: email, password, first/last name, role
- Profile: bio, skills, experience, education, location
- Social: website, LinkedIn, GitHub profiles
- Timestamps: created_at, updated_at

### Job
- Details: title, company, location, type, category
- Requirements: description, requirements, benefits
- Settings: remote, urgent, salary, tags
- Metadata: employer, status, applications count
- Timestamps: posted_at, created_at, updated_at

### Application
- Job details: job_id, job_title, employer_id
- Applicant info: applicant_id, name, email
- Documents: resume, cover_letter
- Status tracking: new, reviewed, interview, etc.
- Timestamps: applied_at, created_at, updated_at

## 🔧 Configuration

The application uses environment-based configuration:

- **Development**: `FLASK_ENV=development` (default)
- **Production**: `FLASK_ENV=production`
- **Testing**: `FLASK_ENV=testing`

### Environment Variables

- `SECRET_KEY`: Application secret key (required for production)
- `DATABASE_URL`: Database connection string
- `FLASK_ENV`: Environment mode

## 📱 Usage Guide

### For Job Seekers

1. **Create Account**: Sign up as a job seeker
2. **Complete Profile**: Add your skills, experience, and portfolio links
3. **Search Jobs**: Use the search bar and filters to find opportunities
4. **Apply**: Submit applications with resume and cover letter
5. **Track Applications**: Monitor status in your dashboard

### For Employers

1. **Create Account**: Sign up as an employer
2. **Post Jobs**: Create detailed job listings
3. **Review Applications**: Manage incoming applications
4. **Track Performance**: Monitor job and application metrics

## 🚀 Deployment

### Local Development
```bash
python run.py
```

### Production Deployment
1. Set environment variables:
   ```bash
   export FLASK_ENV=production
   export SECRET_KEY=your-secure-secret-key
   ```

2. Use a production WSGI server:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

### Docker Deployment
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

## 🧪 Testing

Run the test suite:
```bash
python -m pytest tests/
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

If you encounter any issues:

1. Check the [Issues](https://github.com/your-repo/issues) page
2. Create a new issue with detailed information
3. Contact the development team

## 🗺️ Roadmap

### Phase 1 (Current)
- ✅ Basic job board functionality
- ✅ User authentication and profiles
- ✅ Job posting and applications
- ✅ Search and filtering

### Phase 2 (Next)
- 🔄 Email notifications
- 🔄 Advanced search algorithms
- 🔄 Job recommendations
- 🔄 Mobile app

### Phase 3 (Future)
- 📅 AI-powered job matching
- 📅 Video interviews
- 📅 Skills assessment
- 📅 Analytics dashboard

---

**Built with ❤️ using Flask and modern web technologies**
