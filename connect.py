#!/usr/bin/env python
###
#
# @Name : MongoDbPython/connect.py
# @Version : 1.0
# @Programmer : Max
# @Date : 2018-12
# @Released under : https://github.com/BaseMax/MongoDbPython/blob/master/LICENSE
# @Repository : https://github.com/BaseMax/MongoDbPython
#
###

# Some useful libraries
import pymongo
import json
import os
import sys
client = pymongo.MongoClient("mongodb://localhost:27017/")
#dblist = myclient.list_database_names()
db_name = "name"
db = client[db_name]
