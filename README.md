# Test Project with Django and Frontend Technologies

![Django Logo](https://www.djangoproject.com/m/img/logos/django-logo-negative.png)

## Overview

This is a test project that integrates **Django** as the backend framework with various frontend technologies and **Java Script**. This project serves as a demonstration of building a full-stack application using modern web development practices.

## Features

- **Django Backend**: A robust and scalable backend powered by Django.
- **Frontend Technologies**: Utilizes HTML, CSS, and JavaScript for a responsive and interactive user interface
- **RESTful API**: Provides a RESTful API for seamless communication between frontend and backend.
- **Database Management**: Uses SQLite for local development and PostgreSQL for production.

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Node.js (for frontend dependencies)

### Installation

1. **Clone the repository**:
   ```bash
   git clonehttps://github.com/mahdi-naeeni/first-djando-web-site.git
   cd first-djando-web-site
   ```

2. **Set up a Python virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate  # For Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install frontend dependencies**:
   ```bash
   cd frontend-directory
   npm install
   ```

5. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   Open your browser and go to `http://127.0.0.1:8000`.

## Contributing

Contributions are welcome! Please create a pull request for any improvements or features you want to add.
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Made with 💚 by the Django Community
