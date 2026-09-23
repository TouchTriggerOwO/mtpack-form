from flask import Flask, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)

messages = []


@app.route("/")
def home():
    return "[DEBUG] API_OK"


@app.route("/message", methods=["POST"])
def receive_message():

    data = request.form

    name = data.get("name", "").strip()
    number = data.get("title", "").strip()
    message = data.get("message", "").strip()

    if not name or not title or not message:
        return jsonify({
            "success": False,
            "error": "Заполните все поля"
        }), 400

    new_message = {
        "id": len(messages) + 1,
        "name": name,
        "number": title,
        "message": message,
        "date": datetime.now().isoformat()
    }

    messages.append(new_message)

    return jsonify({
        "success": True,
        "message": "Успешно"
    })


@app.route("/messages", methods=["GET"])
def get_messages():

    return jsonify(messages)


@app.route("/messages/clear", methods=["POST"])
def clear_messages():

    messages.clear()

    return jsonify({
        "success": True
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)