#!/usr/bin/python3
"""Add and save all arguments to a Python list"""
import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


args = sys.argv[1:]
filename = 'add_item.json'
with open(filename, "a+") as f:
    try:
        items = load_from_json_file(filename)
    except Exception:
        items = []


    items.extend(sys.argv[1:])
    save_to_json_file(items, filename)