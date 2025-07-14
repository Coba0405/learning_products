import json
import os

# jsonファイルに名前をつける
TODO_FILE = 'todo.json'
# jsonに読み込む
def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return {}

def add_task():
    

# jsonがなければ作成する

