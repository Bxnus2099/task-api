from flask import Flask, request, jsonify
import jwt
import datetime
import requests
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

# mock user
USER = {
    "username": "student",
    "password": "1234"
}

# mock database
tasks = []

# LOGIN
@app.route('/login', methods=['POST'])
def login():
    data = request.json

    if not data or not data.get("username") or not data.get("password"):
        return jsonify({
            "error": {
                "code": 400,
                "message": "Missing username or password"
            }
        }), 400

    if data["username"] == USER["username"] and data["password"] == USER["password"]:
        token = jwt.encode({
            "user": data["username"],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, app.config['SECRET_KEY'], algorithm="HS256")

        return jsonify({"token": token})

    return jsonify({
        "error": {
            "code": 401,
            "message": "Invalid credentials"
        }
    }), 401


# TOKEN CHECK
def verify_token(req):
    auth = req.headers.get("Authorization")

    if not auth:
        return None, ("Missing token", 401)

    try:
        token = auth.split(" ")[1]
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        return data, None
    except:
        return None, ("Invalid token", 401)

# GET TASKS
@app.route('/tasks', methods=['GET'])
def get_tasks():
    user, error = verify_token(request)
    if error:
        return jsonify({"error": {"code": error[1], "message": error[0]}}), error[1]

    return jsonify({"tasks": tasks})

# CREATE TASK
@app.route('/tasks', methods=['POST'])
def create_task():
    user, error = verify_token(request)
    if error:
        return jsonify({"error": {"code": error[1], "message": error[0]}}), error[1]

    data = request.json

    if not data or not data.get("title"):
        return jsonify({
            "error": {
                "code": 400,
                "message": "Title is required"
            }
        }), 400

    new_task = {
    "id": len(tasks) + 1,
    "title": data["title"],
    "status": data.get("status", "pending"),
    "priority": data.get("priority", "medium"),
    "due_date": data.get("due_date", None)
    }

    tasks.append(new_task)

    return jsonify({"message": "Task created"})


# EXTERNAL API
@app.route('/external-tasks', methods=['GET'])
def external_tasks():
    user, error = verify_token(request)
    if error:
        return jsonify({"error": {"code": error[1], "message": error[0]}}), error[1]

    friend_apis = [
        "https://mini-task-api-v2.onrender.com/",
        "https://flask-api-mini.onrender.com/"
    ]

    external_all = []

    for url in friend_apis:
        try:
            res = requests.get(url, timeout=10)
            data = res.json()
            external_all.append(data)
        except:
            external_all.append({"error": f"Cannot connect to {url}"})

    return jsonify({
        "my_tasks": tasks,
        "external_tasks": external_all
    })


# รองรับ Deploy 
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)