from flask import Flask,jsonify, request

app=Flask(__name__)

tasks = [
    {
        'id': 1,
        'name': u'John',
        'contact': u'john_winter@gmail.com', 
        'done': False
    },
    {
        'id':2,
        'name':'Ricardo',
        'contact':u'971-956-1111',
        'done':False
    }
]

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'name': request.json['name'],
        'contact': request.json.get('contact', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })

if (__name__ == "__main__"):
    app.run(debug=True)