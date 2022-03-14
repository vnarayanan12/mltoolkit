# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 05:37:08 2019

@author: User
"""


import argparse

import os
import pymongo
from pymongo import MongoClient, errors


# use a try-except indentation to catch MongoClient() errors

def main():
    print("Entering the docker ")
    
    parser = argparse.ArgumentParser(description='Process some string.')
    parser.add_argument("folder")
    # parser.add_argument("mongodbURL")
    parser.add_argument("database")
    parser.add_argument("collection")
    args = parser.parse_args()
    # print(args)
   
    inputFolder = args.folder
    # dbUrl = args.mongodbURL
    database = args.database
    collection = args.collection
    
    print ("Input File.. ", inputFolder)
    # print ("DB URL.. ", dbUrl)
    
    connString = os.environ['MONGODB_CONNSTRING']
  
           
    writeToDB(inputFolder,  connString, database, collection)
  
        
    print ("Done")
  
def writeToDB(inputFolder, dbUrl, database, collection):
    print("Inserting data ")
    try:
    # try to instantiate a client instance
        # client = MongoClient(
        #     host = [ str(DOMAIN) + ":" + str(PORT) ],
        #     serverSelectionTimeoutMS = 3000, # 3 second timeout
        #     username = "root",
        #     password = "root",
        # )
        client = pymongo.MongoClient(dbUrl)
    # print the version of MongoDB server if connection successful
        #print ("server version:", client.server_info()["version"])
    
        # get the database_names from the MongoClient()
        database_names = client.list_database_names()
        mydb = client[database]
        mycol = mydb[collection]
          # read the input inputJson file
        for entry in os.listdir(inputFolder):
            if os.path.isfile(os.path.join(inputFolder, entry)):
               
                fileName = os.path.join(inputFolder, entry)
                print (fileName)
        
                mydict = { "fileName": entry , "path": fileName}
                x = mycol.insert_one(mydict)
    
    #print list of the _id values of  the inserted documents:
                print(x.inserted_id)

    except errors.ServerSelectionTimeoutError as err:
        # set the client and DB name list to 'None' and `[]` if exception
        client = None
        database_names = []
    
        # catch pymongo.errors.ServerSelectionTimeoutError
        print ("pymongo ERROR:", err)

    print ("\ndatabases:", database_names)

  
     
main()      