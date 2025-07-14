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

todos = json_load

jsonを読み込む
jsonがないなら空の[]を作る
jsonに書き込む

pythonを起動して選択肢を出す

