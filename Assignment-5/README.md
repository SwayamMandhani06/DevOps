# DevOps Assignment 5 — Docker Compose

## Student Details
- **Name:** Swayam Mandhani
- **PRN / Roll No.:** 123B1B184
- **Class:** B.Tech Computer Engineering
- **Division / Batch:** C / C2
- **Subject:** DevOps (BCE27PE01)
- **Assignment:** 5
- **Report Document:** [123B1B184_Assignment_5_DevOps.pdf](Report/123B1B184_Assignment_5_DevOps.pdf)

## Title
**Multi-Container Orchestration with Docker Compose**

## Aim
To orchestrate and deploy a multi-container web application consisting of a Python Flask web API and a MongoDB NoSQL database using Docker Compose, establishing automated service dependencies, port forwarding, environment variable configuration, custom bridge networking, persistent volume storage, and health check monitoring.

## Overview
A multi-container application built with Docker Compose consisting of a Flask web application and MongoDB database.

## Requirements Demonstrated
- Multi-container application
- Compose services
- Port mapping
- Environment variables
- Custom Docker network
- Named persistent volume
- MongoDB health check
- Flask-to-MongoDB communication
- Container lifecycle management

## Architecture

Browser → Flask Web Container → Docker Compose Network → MongoDB Container → MongoDB Volume

## Project Structure

```text
Assignment-5/
├── app/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .dockerignore
├── compose.yaml
├── README.md
├── Report/
│   └── 123B1B184_Assignment_5_DevOps.pdf
└── Screenshots/
    ├── 1-docker-compose-configuration-validation.png
    ├── 2-docker-compose-build.png
    ├── 3-multi-container-application.png
    ├── 4-flask-web-application.png
    ├── 5-application health.png
    ├── 6-flask-mongodb-communication.png
    ├── 7-docker-compose-logs.png
    ├── 8-docker-compose-network (1).png
    ├── 8-docker-compose-network (2).png
    ├── 9-mongodb-persistent-volume.png
    ├── 10-mongodb-stored-data.png
    ├── 11-volume-persistence-verification.png
    └── 12-docker-shutdown.png
```

## Services

| Service | Image / Build | Port | Purpose |
|---|---|---:|---|
| web | Flask app (`./app`) | 5000:5000 | Web/API service |
| mongodb | mongo:7 | 27017:27017 | Database service |

## Environment Variables

The `web` service uses:
- `MONGO_URI=mongodb://mongodb:27017/assignment5`
- `MONGO_DB=assignment5`
- `MONGO_COLLECTION=messages`

MongoDB uses:
- `MONGO_INITDB_DATABASE=assignment5`

## Volume

Named volume:

```text
assignment-5_mongodb-data
```

Mounted inside MongoDB at:

```text
/data/db
```

## Network

Custom Compose bridge network:

```text
assignment-5_assignment5-network
```

The Flask service connects to MongoDB using the Compose service name:

```text
mongodb
```

## Run the Application

```powershell
docker compose config
docker compose build
docker compose up -d
docker compose ps
```

## Test Endpoints

Open:

```text
http://localhost:5000
http://localhost:5000/health
http://localhost:5000/data
```

`/health` verifies the Flask-to-MongoDB connection.

`/data` inserts a document into MongoDB and returns stored records.

## Inspect Logs

```powershell
docker compose logs --tail=50
```

## Inspect Network

```powershell
docker network ls
docker network inspect assignment-5_assignment5-network
```

## Inspect Volume

```powershell
docker volume ls
docker volume inspect assignment-5_mongodb-data
```

## Verify MongoDB Data

```powershell
docker compose exec mongodb mongosh
```

Then:

```javascript
use assignment5
show collections
db.messages.find().pretty()
exit
```

## Verify Persistence

```powershell
docker compose restart mongodb
docker compose ps
docker compose exec mongodb mongosh
```

Then:

```javascript
use assignment5
db.messages.find().pretty()
exit
```

The previously inserted record remains available because MongoDB uses the named Docker volume.

## Stop the Application

```powershell
docker compose down
```

This removes the containers and Compose network while retaining the named volume.

To remove the volume as well:

```powershell
docker compose down -v
```

## Result

The Flask and MongoDB services were successfully orchestrated using Docker Compose. Service configuration, ports, environment variables, networking, persistent storage, health checks, database communication, and container lifecycle operations were successfully demonstrated.

## Screenshot Evidence

| Figure | Screenshot | Purpose |
|---|---|---|
| 1 | [`1-docker-compose-configuration-validation.png`](Screenshots/1-docker-compose-configuration-validation.png) | Docker Compose specification validation via `docker compose config` |
| 2 | [`2-docker-compose-build.png`](Screenshots/2-docker-compose-build.png) | Web service container image build via `docker compose build` |
| 3 | [`3-multi-container-application.png`](Screenshots/3-multi-container-application.png) | Multi-container application execution and container status (`docker compose up -d` & `ps`) |
| 4 | [`4-flask-web-application.png`](Screenshots/4-flask-web-application.png) | Flask web application home endpoint response (`http://localhost:5000`) |
| 5 | [`5-application health.png`](Screenshots/5-application%20health.png) | Application and MongoDB connectivity health check (`http://localhost:5000/health`) |
| 6 | [`6-flask-mongodb-communication.png`](Screenshots/6-flask-mongodb-communication.png) | Document insertion and retrieval endpoint (`http://localhost:5000/data`) |
| 7 | [`7-docker-compose-logs.png`](Screenshots/7-docker-compose-logs.png) | Multi-container runtime logs inspection via `docker compose logs` |
| 8a | [`8-docker-compose-network (1).png`](Screenshots/8-docker-compose-network%20%281%29.png) | Docker network listing (`docker network ls`) showing custom network |
| 8b | [`8-docker-compose-network (2).png`](Screenshots/8-docker-compose-network%20%282%29.png) | Docker network inspection (`docker network inspect assignment-5_assignment5-network`) |
| 9 | [`9-mongodb-persistent-volume.png`](Screenshots/9-mongodb-persistent-volume.png) | Persistent volume inspection (`docker volume inspect assignment-5_mongodb-data`) |
| 10 | [`10-mongodb-stored-data.png`](Screenshots/10-mongodb-stored-data.png) | Stored document records verified inside MongoDB shell (`mongosh`) |
| 11 | [`11-volume-persistence-verification.png`](Screenshots/11-volume-persistence-verification.png) | Volume persistence verification across MongoDB container restart |
| 12 | [`12-docker-shutdown.png`](Screenshots/12-docker-shutdown.png) | Graceful application shutdown via `docker compose down` |

## Submission

**GitHub:** https://github.com/SwayamMandhani06/DevOps/tree/main/Assignment-5

**Hosted / Output:** N/A — Multi-container application executed locally.
