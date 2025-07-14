import json
import os
import sys
from typing import List

# jsonファイルに名前をつける
TODO_FILE = 'todo.json'
# jsonに読み込む
def load_tasks() -> List[str]:
    if not os.path.exists(TODO_FILE):
        return []
    try:
        with open(TODO_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_task(todos: List[str]) -> None:
    with open(TODO_FILE, 'w', encoding='utf-8') as file:
            json.dump(todos, file, ensure_ascii=False, indent=4)

def show_task(todos: List[str]) -> None:
    if not todos:
        print('Todoリストは空です')
    else:
        for i, task in enumerate(todos, start=1):
            print(f"{i}. {task}")

def main() -> None:
    todos = load_tasks()

print("1. Todoを追加")
print("2. Todoを表示")
print("3. Todoを削除")
print("4. Todoリストを修了")
while True:
    try:
        choice = int(input('番号を入力してください'))
    except ValueError:
        print("無効な値です。数字を入力してください")
        continue
    if choice == 1:
        task = input("Todoを入力してください")
        if task:
            todos.append(task)
            add_task(todos)
        print("Todoを保存しました")
    elif choice == 2:
        for todo in todos:
            print(todo)
        # for i, todo in enumerate(todos, 1):
        #     print(i, todo)
    elif choice == 3:
        try:
            delete_choice = int(input("削除するTodoの番号を入力してください"))
            del todos[delete_choice - 1]
            print("todoを削除しました")
        except IndexError:
            print("エラー: その番号のtodoは存在しません")
        except ValueError:
            print("エラー: 数字を入力してください")
        add_task(todos)
        print("todoリストを保存しました")
    elif choice == 4:
        add_task(todos)
        print("todoアプリを終了します")
        break
    else:
        print('無効な値です')
