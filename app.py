import json
from flask import Flask, request
from bson import json_util, ObjectId
import pymongo
from configuration import *

app = Flask(__name__)

client = pymongo.MongoClient(connection_url)
Database = client.get_database(database_name)
Collection = Database[collection_name]


@app.route('/')
def home():
    return 'AGH Space Systems Server'


@app.route('/getAll', methods=['GET'])
def get_all():
    result = Collection.find()
    if result is None:
        return json_util.dumps(result)
    pretty_docs=[prettify_document(json.loads(json_util.dumps(doc))) for doc in result]
    return str(pretty_docs)


@app.route('/getOne/<id>', methods=['GET'])
def get_one(id):
    result = Collection.find_one({"_id": ObjectId(id)})
    if result is None:
        return json_util.dumps(result)
    return prettify_document(json.loads(json_util.dumps(result)))

def prettify_document(json_document):
    json_document["_id"] = str(json_document["_id"]["$oid"])
    return json_document


@app.route('/delete/<id>')
def delete(id):
    return str(Collection.delete_one({"_id": ObjectId(id)}).acknowledged)


@app.route('/addOne', methods=['POST'])
def add_one():
    document=request.get_json()
    return str(Collection.insert_one(document).inserted_id)


if __name__ == '__main__':
    app.run(debug=True, port=port)
