# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 05:37:08 2019

@author: User
"""

import json
import argparse
import pymongo
import os

def main():
    
    parser = argparse.ArgumentParser(description='Process some string.')
    parser.add_argument("file")
    parser.add_argument("mongodb")
    args = parser.parse_args()
    print(args)
   
    inputFolder = args.file
    dbUrl = args.mongodb
    
    print ("Input File.. ", inputFolder)
    print ("DB URL.. ", dbUrl)
    
   
    data = {}
    data['Results'] = []
    # read the input inputJson file
    readInput(inputFolder, dbUrl)
  
        
    print ("Done")
  
def writeToDB(fileName, data, dbUrl):
    print("Inserting data ")

    # myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    myclient = pymongo.MongoClient(dbUrl)
    mydb = myclient["audioFiles"]
    mycol = mydb["fileName"]

    mydict = { "fileName": fileName , "path": data}
    x = mycol.insert_one(mydict)
    
    #print list of the _id values of the inserted documents:
    print(x.inserted_id)
        
def writeToJson(data, outPath):
    with open(outPath, 'w') as outfile:
        json.dump(data, outfile)
        
 
def readInput(inputJson, dbUrl):
   
   
    for entry in os.listdir(inputJson):
        if os.path.isfile(os.path.join(inputJson, entry)):
           
            fileName = os.path.join(inputJson, entry)
            print (fileName)
           
            writeToDB(inputJson, fileName, dbUrl)
     
main()      