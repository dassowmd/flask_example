from flask import Flask, request
from flask import render_template
from bson.json_util import dumps
from bson.objectid import ObjectId
import mongo_layer

app = Flask(__name__)

mongo_obj = mongo_layer.mongo_obj()
@app.route('/', methods=['GET'])
def home_page(name=None):
    return render_template('hello.html', name=name)

@app.route('/api/courses/<id>', methods=['GET'])
def get_course(id):
    return dumps(mongo_obj.query_course(query_params={'_id': ObjectId(id)}))

@app.route('/api/courses/', methods=['POST'])
def insert_course():
    body = request.get_json()
    return dumps(mongo_obj.insert_course(course=body))

@app.route('/api/courses/<id>', methods=['PUT'])
def update_course(id):
    body = request.get_json()
    return dumps(mongo_obj.update_course(id=ObjectId(id), course=body))

if __name__ == '__main__':
    app.run()