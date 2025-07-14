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

def add_task(todos):
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'w') as file:
            json.dump(todos, file, ensure_ascii=False, indent=4)

todos = load_tasks

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
        todo = input("Todoを入力してください")
        todos.append(todo)
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
        except E
