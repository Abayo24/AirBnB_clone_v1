#!/usr/bin/python3
"""init file"""
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
