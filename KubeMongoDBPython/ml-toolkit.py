# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 15:43:39 2022

@author: vijin
"""

from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

import socket
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
@app.route("/audio_files", methods=["POST"])
def create_file(data):
    data = request.get_json(force=True)
    db.audio_files.insert_one(data)
    return jsonify(
        message="Task saved successfully!"
    )


def getFileandIngestIntoDB(inputFile, path):
   
    print ("Input File.. ", inputFile)
    # print ("DB URL.. ", dbUrl)
    
    #data = request.get_json(force=True)
    mydict = { "fileName": inputFile , "filePath": path}
    create_file(mydict)
    return jsonify(
        message="File saved successfully!"
    )
    print ("Done")
  
  
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)