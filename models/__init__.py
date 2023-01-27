#!/usr/bin/python3
"""This module instantiates an object of class FileStorage or DBStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
import os

storageType = os.environ.get('HBNB_TYPE_STORAGE')
if storageType == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
