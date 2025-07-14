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

def add_task(todo):
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'w') as file:
            json.dump(todo, file, ensure_ascii=False, indent=4)

todo = load_tasks

print("1. Todoを追加")
