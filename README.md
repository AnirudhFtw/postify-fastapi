# 🚀 Postify – Scalable Social Media Backend API

Postify is a **production-ready, high-performance RESTful API** designed for a social media platform. Built with **FastAPI**, it emphasizes **scalability, modular design, and clean architecture**, making it suitable for real-world deployment and extensibility.

It follows industry best practices such as **layered architecture, dependency injection, and containerization**, ensuring maintainability and ease of scaling.

---

## ✨ Features

- 🔐 **JWT Authentication**  
  Secure user authentication using JSON Web Tokens. Supports login, registration, and protected routes with token-based access control.

- 👤 **User Management**  
  Handles user creation, authentication, and identity management with proper password hashing and validation.

- 📝 **Post Management (CRUD)**  
  Users can create, retrieve, update, and delete posts with ownership-based access control.

- ❤️ **Social Interactions**  
  Like and Unlike functionality allowing users to engage with posts dynamically.

- 🧾 **Data Validation with Pydantic**  
  Ensures strict request and response validation, reducing runtime errors and enforcing schema consistency.

- 🗄️ **Robust Database Layer**  
  Uses PostgreSQL for relational data storage and SQLAlchemy ORM for efficient database operations.

- ⚡ **FastAPI Performance**  
  Built on asynchronous capabilities, delivering high performance and low latency.

- 🐳 **Dockerized Deployment**  
  Fully containerized application for consistent development and production environments.

---

## 🛠️ Tech Stack

| Category | Technology |
| :--- | :--- |
| **Framework** | [FastAPI](https://fastapi.tiangolo.com/) |
| **Database** | [PostgreSQL](https://www.postgresql.org/) |
| **ORM** | [SQLAlchemy](https://www.sqlalchemy.org/) |
| **Validation** | [Pydantic](https://docs.pydantic.dev/) |
| **Authentication** | JWT (JSON Web Tokens) |
| **DevOps** | [Docker](https://www.docker.com/) |

---

## 📂 Project Structure

```text
postify-fastapi/
│── app/
│   ├── models/        # SQLAlchemy database models (tables & relationships)
│   ├── schemas/       # Pydantic data schemas
│   ├── routes/        # API endpoint controllers
│   ├── database/      # DB connection and session logic
│   └── utils/         # Password hashing & JWT helpers
│── Dockerfile         # Docker configuration
│── requirements.txt   # Python dependencies
│── main.py            # Application entry point
└── .env               # Environment variables (not tracked)
```

---

## ⚙️ Environment Variables

Create a `.env` file in the root directory:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/postify
SECRET_KEY=your_super_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 📦 Installation & Setup

### 🔹 Run with Docker (Recommended)

```bash
# Clone the repository
git clone https://github.com/AnirudhFtw/postify-fastapi.git

# Navigate into the project directory
cd postify-fastapi

# Build Docker image
docker build -t postify .

# Run the container
docker run -d -p 8000:8000 postify
```

---

## 📬 API Testing with Postman

You can test all API endpoints using **Postman**.

### Steps:

1. Open Postman  
2. Create a new request  
3. Set method (GET, POST, PUT, DELETE)  
4. Enter URL:  
   `http://localhost:8000`  

5. For protected routes, add headers:

```http
Authorization: Bearer <your_token>
```

6. Send request and view response  

---

## 🔐 Authentication Flow

1. User registers or logs in  
2. Server returns a JWT token  
3. Client includes token in headers  
4. Protected routes validate the token before granting access  

---

## 🔄 Example API Flow

- Register User → `/register`  
- Login User → `/login`  
- Create/See/Delete/Update Post → `/posts`  
- Like Post → `/like/{post_id}`  

---


## 👨‍💻 Author

**Anirudh Gupta**

---
