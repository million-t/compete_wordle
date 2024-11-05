# 🎉 Django Wordle Competition 🎉

This is a Django-based api for managing and participating in Wordle competitions. The application includes features such as user authentication, real-time standings, and integration with a Redis server for caching and WebSocket communication.

## 📋 Table of Contents

- [✨ Features](#-features)
- [🛠 Technologies](#-technologies)
- [🚀 Setup](#-setup)
- [📚 Usage](#-usage)
- [🔧 Environment Variables](#-environment-variables)
- [🐳 Docker](#-docker)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)

## ✨ Features

- 🔐 User authentication and authorization
- 📊 Real-time standings using WebSockets
- ⚡ Integration with Redis for caching and WebSocket communication
- 🌐 RESTful API for managing Wordle competitions
- 🛠 Admin interface for managing users and competitions

## 🛠 Technologies

- 🐍 Django
- 🌐 Django REST Framework
- 🔌 Django Channels
- 🐘 Redis
- 🐘 PostgreSQL (Neon serverless PostgreSQL)
- 🐳 Docker
- 🐳 Docker Compose

## 🚀 Setup

### Prerequisites

- 🐍 Python 3.11
- 🐳 Docker
- 🐳 Docker Compose

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Create a .env file in the project root and add the necessary environment variables (see Environment Variables).

5. Apply the migrations:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
6. Collect static files:
    ```
    python manage.py collectstatic --noinput
    ```

## 🔧 Environment Variables
Create a .env file in the project root with the following content:
    ```
    DATABASE_URL=db-connection-string
    SECRET_KEY=django-secret-key
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1,production-app-url
    REDIS_URL=redis://redis:6379
    ```

## 🐳 Docker
1. Build and run the Docker containers:
    ```
    docker-compose up --build
    ```
2. Access the application at http://localhost:8000.

## 📚 Usage
Running the Development Server
To run the development server, use the following command:
    ```
    python manage.py runserver
    ```

Running Tests (In Progress)
To run the tests, use the following command:
    ```
    python manage.py test
    ```

## 🤝 Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes.

## 📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

