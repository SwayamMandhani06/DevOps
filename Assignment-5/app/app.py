import os
from datetime import datetime, timezone

from flask import Flask, jsonify
from pymongo import MongoClient
from pymongo.errors import PyMongoError

app = Flask(__name__)

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/assignment5")
MONGO_DB = os.getenv("MONGO_DB", "assignment5")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION", "messages")

client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]


@app.route("/")
def home():
    return jsonify({
        "application": "DevOps Assignment 5",
        "message": "Flask web application is running with Docker Compose.",
        "database": "MongoDB",
        "endpoints": ["/", "/health", "/data"]
    })


@app.route("/health")
def health():
    try:
        client.admin.command("ping")
        return jsonify({
            "status": "healthy",
            "web_service": "running",
            "database_service": "connected"
        }), 200
    except PyMongoError as exc:
        return jsonify({
            "status": "unhealthy",
            "web_service": "running",
            "database_service": "unavailable",
            "error": str(exc)
        }), 503


@app.route("/data")
def data():
    try:
        document = {
            "message": "Hello from Flask to MongoDB!",
            "created_at": datetime.now(timezone.utc).isoformat()
        }
        result = collection.insert_one(document)

        documents = list(
            collection.find({}, {"_id": 0}).sort("_id", -1).limit(5)
        )

        return jsonify({
            "status": "success",
            "inserted_id": str(result.inserted_id),
            "database": MONGO_DB,
            "collection": MONGO_COLLECTION,
            "records": documents
        }), 200

    except PyMongoError as exc:
        return jsonify({
            "status": "error",
            "message": "Could not communicate with MongoDB.",
            "error": str(exc)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
