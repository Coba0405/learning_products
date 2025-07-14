import json
import os

# jsonファイルに名前をつける
TODO_FILE = 'todo.json'
# jsonに書き込む
def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            

# jsonがなければ作成する

