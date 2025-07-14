import json
import os

# jsonファイルに名前をつける
TODO_FILE = 'todo.json'
# json
def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)

# jsonがなければ作成する

