#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

ty_sto = os.getenv('HBNB_TYPE_STORAGE')
if ty_sto == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
