import json

TODO_LIST = 'todo_lost.json'

def load_tasks():
    try:
        with open(TODO_LIST, 'r', encoding='utf-8') as file:
            return json.load(file)
    except:
        return []

def save_tasks(todos):
    with open(TODO_LIST, 'w', encoding='utf-8') as file:
        json.dump(todos, file, ensure_ascii=False, indent=4)

todos = load_tasks()

print("1. Todoを追加")
print("2. Todoを表示")
print("3. Todoを削除")
print("4. 終了")

while 
