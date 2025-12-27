# E-commerce
## 🛒 E-Commerce Backend API

• Production-ready E-Commerce REST API built with Django Rest Framework, Docker, and Celery.

• Designed for scalability, security, and modern backend architectures.


## 🌐 Live Swagger API Documentation

👉 https://elixya.uz


## ✨ Overview

• This project is a fully-featured backend service for an e-commerce platform, providing secure authentication, product management, background task processing, and API documentation via Swagger.

• The system follows modern backend best practices and is fully containerized for easy deployment.


## 🧱 Tech Stack

• Python 3.13

• Django 5.2

• Django Rest Framework

• JWT Authentication (SimpleJWT)

• Djoser

• Celery

• RabbitMQ

• Redis

• Docker & Docker Compose

• Nginx

• Swagger (drf-yasg)

• SQLite (Development)


## 🚀 Key Features

• 🔐Secure JWT authentication 
• 👤Custom user model 
• 📦Products & categories management 
• 💳Payment integration 
• 📲SMS-based authentication
• 📬Email notifications
• ⚙️Background tasks with Celery
• 📖Interactive Swagger API docs
• 🔒HTTPS with Let’s Encrypt
• 🐳Fully Dockerized production setup


## 📌 API Documentation

All endpoints are documented using Swagger UI.

## 📍 Access here

👉 https://elixya.uz


## 🐳 Getting Started (Docker)

** 1️⃣ Clone Repository:

• git clone https://github.com/eliksaidaliev9/E-commerce.git

• cd E-commerce


2️⃣ Environment Variables:

Create a .env file:

• SECRET_KEY=your_secret_key

• EMAIL_HOST_USER=your_email

• EMAIL_HOST_PASSWORD=your_password

• CELERY_BROKER_URL=amqp://guest:guest@rabbitmq:5672//

• CELERY_RESULT_BACKEND=redis://redis:6379/0

3️⃣ Build & Run:

• docker-compose up -d --build

## 🔐 Authentication

• Uses JWT Bearer Token authentication.

• Authorization: Bearer <access_token>

## 🧠 Author

Elyor Mahamadjanov

Backend Developer 

🌐 Website: https://elixya.uz

📧 Email: elik.saidaliev9@gmail.com

💼 GitHub: https://github.com/eliksaidaliev9


## ⭐️ Support

If you find this project useful, please consider giving it a ⭐️ on GitHub.
