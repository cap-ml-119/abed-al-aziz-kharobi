from flask import Flask
import uuid
app = Flask(__name__)

# local date base : empty array we are added the data to it
todo = []

'#add endpoint'


@app.route('/post/<string:name>/<string:status>', methods=['POST'])
def add(name, status):
    todo.append({"name": name, "uid": uuid.uuid4().int, "status": status})
    return "added"


'#update endpoint'


@app.route('/update/<int:id>/<string:name>/<string:status>', methods=['PUT'])
def update(id, name, status):
    for i in todo:
        if(i["uid"] == id):
            i["name"] = name
            i["status"] = status
    return "is update"

# update the status by id


@app.route('/update/<int:id>/<string:status>', methods=['PUT'])
def update_status(id, status):
    for i in todo:
        if(i["uid"] == id):
            i["status"] = status


'#get endpoint to test review my data'


@app.route('/get', methods=['GET'])
def re():
    return str(todo)


'#run the flask'

if __name__ == "__main__":
    app.run(debug=True)
