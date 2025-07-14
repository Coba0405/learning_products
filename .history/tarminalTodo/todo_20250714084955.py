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

while True:
    try:
        choice = int(input("番号を選択してください: "))
    except ValueError:
        print("数字を入力してください")
        continue
    if choice == 1:
        todo =input("Todoを入力してください")
        todos.append(todo)
    elif choice ==2:
        for todo in enumerate(todos, 1)
        print(todo)
    elif choice == 3:
        try:
            delete_choice = int(input('削除したい番号を選択してください: '))
            del todos
