# DevOps Assignment 5 — Docker Compose

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
└── README.md
```

## Services

| Service | Image / Build | Port | Purpose |
|---|---|---:|---|
| web | Flask app | 5000 | Web/API service |
| mongodb | mongo:7 | 27017 | Database service |

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

## Repository

https://github.com/SwayamMandhani06/DevOps/tree/main/Assignment-5

