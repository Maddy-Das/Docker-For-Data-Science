# 🚀 Docker + Flask + Redis Projects

This repository contains **two beginner-friendly Docker projects**:

1. **Flask Project (Docker Only)** → A simple *Hello World* Flask app inside a Docker container.
2. **Flask + Redis Project (Docker Compose)** → A Flask app connected to Redis using Docker Compose.

These examples are great for **data engineers and web developers** to understand the basics of Docker.

---

## 1️⃣ Flask Project (Docker Only)

### **app.py**

Your Flask application file.

### **Dockerfile**

```dockerfile
FROM python:3.8-alpine          # Lightweight Python base image
COPY . /app1                    # Copy project files into container
WORKDIR /app1                   # Set working directory
RUN pip install -r requirements.txt   # Install dependencies
CMD ["python", "app.py"]        # Start Flask app
```

👉 Important: Use `CMD ["python", "app.py"]` (not `CMD app.py`).

### **requirements.txt**

```
flask
```

---

### ▶️ Run the Flask Project

1. **Build the image**

   ```bash
   docker build -t welcome-app .
   ```

2. **Run the container**

   ```bash
   docker run -p 8000:5001 welcome-app
   ```

3. **Open in browser** → [http://localhost:8000](http://localhost:8000)

4. **Stop & clean up**

   ```bash
   docker ps -a
   docker stop <container_id>
   docker rmi -f <image_id>
   ```

---

## 2️⃣ Flask + Redis Project (Docker Compose)

### **app.py**

Flask app with Redis integration.

### **Dockerfile**

(Same as Flask-only project)

### **docker-compose.yml**

Defines both Flask (web) and Redis services.

### **requirements.txt**

```
flask
redis
```

---

### ▶️ Run the Compose Project

1. **Build & start services**

   ```bash
   docker compose up --build
   ```

2. **Open in browser** → [http://localhost:8000](http://localhost:8000)

   Example output:

   ```
   Hello Maddy! I have been seen 1 times.
   ```

3. **Stop services**

   ```bash
   docker compose stop
   ```

4. **Remove containers**

   ```bash
   docker compose down
   ```

---

## 🐳 Common Docker Commands

| Command                               | Description               |
| ------------------------------------- | ------------------------- |
| `docker build -t welcome-app .`       | Build image               |
| `docker run -p 8000:5001 welcome-app` | Run container             |
| `docker rmi -f <id>`                  | Remove image              |
| `docker images`                       | List images               |
| `docker ps -a`                        | List all containers       |
| `docker compose up`                   | Start services            |
| `docker compose build`                | Build images for services |
| `docker compose stop`                 | Stop services             |

---

## ❌ Common Issues & Fixes

* **Typo in command** → Check spelling (`docker`, not `doker`).
* **Port already in use** → Change port mapping (e.g., `9000:5000`).
* **Module not found** → Rebuild with `docker compose up --build`.
* **Redis connection error** → Wait a few seconds (Redis needs time to start).

---

## ✅ What I’ll Learn

* How to run a **Flask app inside Docker**
* How to use **Docker Compose with Flask + Redis**

---
