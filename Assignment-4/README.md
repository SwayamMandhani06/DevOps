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
├── README.md
├── Report/
│   └── 123B1B184_Assignment_4_DevOps.pdf
└── Screenshots/
    ├── 0-docker-verification (1).png
    ├── 0-docker-verification.png
    ├── 1-local-flask.png
    ├── 2-flask-healthy.png
    ├── 3-docker-build.png
    ├── 4-docker-images.png
    ├── 5-docker-run.png
    ├── 6-dockerized-running.png
    ├── 7-dockerized-health-check.png
    ├── 8-docker-container-logs.png
    ├── 9-applications-inside-docker.png
    ├── 10-stopping-and-checking-status-of-container.png
    ├── 11-restart-docker-container.png
    ├── 12-container-removed.png
    └── 13-docker-image-cleanup.png
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

| Figure | Screenshot | Purpose |
|---|---|---|
| 0a | [`0-docker-verification.png`](Screenshots/0-docker-verification.png) | Docker installation and version verification |
| 0b | [`0-docker-verification (1).png`](Screenshots/0-docker-verification%20%281%29.png) | Docker `hello-world` test container execution |
| 1 | [`1-local-flask.png`](Screenshots/1-local-flask.png) | Local Flask application execution |
| 2 | [`2-flask-healthy.png`](Screenshots/2-flask-healthy.png) | Local `/health` endpoint response |
| 3 | [`3-docker-build.png`](Screenshots/3-docker-build.png) | Successful Docker image build (`flask-docker-app:v1`) |
| 4 | [`4-docker-images.png`](Screenshots/4-docker-images.png) | Local `docker images` repository listing |
| 5 | [`5-docker-run.png`](Screenshots/5-docker-run.png) | Running container in detached mode with port mapping (`5000:5000`) |
| 6 | [`6-dockerized-running.png`](Screenshots/6-dockerized-running.png) | Dockerized application output in browser (`http://localhost:5000`) |
| 7 | [`7-dockerized-health-check.png`](Screenshots/7-dockerized-health-check.png) | Dockerized `/health` endpoint verification (`http://localhost:5000/health`) |
| 8 | [`8-docker-container-logs.png`](Screenshots/8-docker-container-logs.png) | Container runtime execution logs via `docker logs` |
| 9 | [`9-applications-inside-docker.png`](Screenshots/9-applications-inside-docker.png) | Interactive container shell inspection (`pwd`, `ls`) |
| 10 | [`10-stopping-and-checking-status-of-container.png`](Screenshots/10-stopping-and-checking-status-of-container.png) | Container stop and status check (`docker ps -a`) |
| 11 | [`11-restart-docker-container.png`](Screenshots/11-restart-docker-container.png) | Container restart verification via `docker start` |
| 12 | [`12-container-removed.png`](Screenshots/12-container-removed.png) | Container removal via `docker rm` |
| 13 | [`13-docker-image-cleanup.png`](Screenshots/13-docker-image-cleanup.png) | Docker image cleanup via `docker rmi` |

## Submission
**GitHub:** https://github.com/SwayamMandhani06/DevOps/tree/main/Assignment-4

**Hosted / Output:** N/A — Docker application executed locally.
