# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 15:43:39 2022

@author: vijin
"""

from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

import socket
import os
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongo:27017/dev"
mongo = PyMongo(app)
db = mongo.db

@app.route("/")
def index():
    hostname = socket.gethostname()
    return jsonify(
        message="Welcome to ML Toolkit  app! I am running inside {} pod!".format(hostname)
    )
@app.route("/audio_files")
def get_all_audio_files():
    audio_files = db.audo_files.find()
    data = []
    for filename in audio_files:
        item = {
            "id": str(audio_files["_id"]),
            "fileName": audio_files["fileName"],
            "filePath": audio_files["filePath"]
        }
        data.append(item)
    return jsonify(
        data=data
    )
  

@app.route("/audio_file", methods=["POST"])
def create_files():
   
    # print ("DB URL.. ", dbUrl)
    
    data = request.get_json(force=True)
    db.audio_files.insert_one({"audio_files": data["audio_files"]})
    #db.audio_files.insert_one(data)
    return jsonify(
        message="Task saved successfully!"
    )

@app.route("/task", methods=["POST"])
def create_task():
    data = request.get_json(force=True)
    db.task.insert_one({"task": data["task"]})
    return jsonify(
        message="Task saved successfully!"
    )

@app.route("/update_file/<id>", methods=["PUT"])
def update_file(id):
    data = request.get_json(force=True)["filePath"]
    response = db.audo_files.update_one({"_id": ObjectId(id)}, {"$set": {"filePath": data}})
    if response.matched_count:
        message = "File Path updated successfully!"
    else:
        message = "No File found!"
    return jsonify(
        message=message
    ) 

@app.route("/audio_files/delete", methods=["POST"])
def delete_all_files():
    db.task.remove()
    return jsonify(
        message="All Files deleted!"
    )
  
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)