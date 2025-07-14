import json

TODO_LIST = 'todo_lost.json'

def json_load():
    try:
        with open(TODO_LIST, 'r', encoding='utf-8') as file:
            return json_load(file)
    except:
        return []

def save_
jsonを読み込む
jsonがないなら空の[]を作る
jsonに書き込む

pythonを起動して選択肢を出す

