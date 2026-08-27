from flask import Flask, request, jsonify
import os

app = Flask(__name__)

API_TOKEN = os.getenv("API_TOKEN")


@app.route("/")
def home():
    return jsonify({
        "status": True,
        "message": "Lecture API is running"
    })


@app.route("/pw")
def pw():
    url = request.args.get("url")
    token = request.args.get("token")

    if not url or not token:
        return jsonify({
            "status": False,
            "message": "url and token are required"
        }), 400

    if token != API_TOKEN:
        return jsonify({
            "status": False,
            "message": "Invalid token"
        }), 401

    return jsonify({
        "status": True,
        "url": url
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
