#!/usr/bin/python3
"""Instantiates a storage object.
"""
import models
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
