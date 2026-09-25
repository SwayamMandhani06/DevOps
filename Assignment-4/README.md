# DevOps Assignment 4 — Create or Migrate an Application to Docker

## Student Details
- **Name:** Swayam Mandhani
- **PRN / Roll No.:** 123B1B184
- **Class:** B.Tech Computer Engineering
- **Division / Batch:** C / C2
- **Subject:** DevOps (BCE27PE01)
- **Assignment:** 4
- **Report Document:** [123B1B184_Assignment_4_DevOps.pdf](Report/123B1B184_Assignment_4_DevOps.pdf)

## Title
**Create or Migrate an Application to Docker**

## Aim
To package a Python Flask application and its dependencies into a Docker image, run it in a Docker container, verify the application through port mapping, inspect logs and container contents, demonstrate the container lifecycle, and clean up Docker resources.

## Technologies
Python 3.12, Flask, Docker Desktop, Dockerfile, PowerShell.

## Project Structure
```text
Assignment-4/
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```

## Application
- `/` — main application response
- `/health` — health-check endpoint
- Application port: `5000`
- Flask binds to `0.0.0.0:5000` for container access.

## Dockerfile
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

## Execution
```powershell
docker --version
docker info
docker run hello-world

pip install -r requirements.txt
python app.py

docker build -t flask-docker-app:v1 .
docker images

docker run -d -p 5000:5000 --name flask-container flask-docker-app:v1
docker ps
```

Open:
```text
http://localhost:5000
http://localhost:5000/health
```

## Logs and Container Inspection
```powershell
docker logs flask-container
docker exec -it flask-container sh
pwd
ls
exit
```

## Lifecycle
```powershell
docker stop flask-container
docker ps
docker ps -a

docker start flask-container
docker ps
```

## Cleanup
```powershell
docker stop flask-container
docker rm flask-container
docker rmi flask-docker-app:v1
docker images
```

## Result
The Flask application was successfully migrated to Docker. The image `flask-docker-app:v1` was built successfully and the application was run in `flask-container` with port `5000:5000`. The application and `/health` endpoint were verified, container logs and internal files were inspected, the container was restarted successfully, and the assignment resources were cleaned up.

## Screenshot Evidence
1. Local Flask application
2. Local `/health`
3. Successful Docker build
4. `docker images`
5. Running container and port mapping
6. Dockerized application
7. Dockerized `/health`
8. Container logs
9. Container shell inspection
10. Container stop/status
11. Container restart
12. Container removal
13. Docker image cleanup

## Submission
**GitHub:** https://github.com/SwayamMandhani06/DevOps/tree/main/Assignment-4

**Hosted / Output:** N/A — Docker application executed locally.
