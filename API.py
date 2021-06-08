from flask import Flask, jsonify, request

app = Flask(__name__)
tasks=[
    {
        "id": 1,
        "contact":"9831702146",
        "name": "Katniss",
        "done": False
    },
    {
        "id": 2,
        "contact": "8130718796",
        "name": "Peeta",
        "done": False
    }
]
@app.route("/")
def default():
    return "Open either http://127.0.0.1:5000/add-data or http://127.0.0.1:5000/get-data to see the API's."

@app.route("/add-data", methods = ["POST"])
def add_data():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data in the accurate format.",
        },400)
    task = {
        "id": tasks[-1]["id"] + 1,
        "contact": request.json["contact"],
        "name": request.json.get("name"),
        "done": False
    }
    tasks.append(task)
    return jsonify({
            "status": "sucess",
            "message": "The task was succesfully added. You can go to http://127.0.0.1:5000/get-data to see the change.",
        })

@app.route("/get-data")
def get_data():
    return jsonify({
        "data": tasks
    })

if __name__=="__main__":
    app.run()