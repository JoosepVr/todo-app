import functions
import time


time_now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"Is is, {time_now}")
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()
        todos.append(todo + "\n")
        functions.write_todos(todos, "todos.txt")

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        # new_todos = [item.strip('\n') for item in todos] # Takes away enter between list.

        for index, item in enumerate(todos):  # Shows the index and items from the list
            item = item.strip('\n') # Takes away enter between list.
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number -= 1

            todos = functions.get_todos()

            new_todo = input('Enter new todo: ') + "\n"
            todos[number] = new_todo
            functions.write_todos(todos)
        except IndexError or ValueError:
            print("Please enter the TODO number, not words!")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            removed = todos.pop(number - 1).strip('\n')

            functions.write_todos(todos)

            message = f"Todo {removed} was removed from list."
            print(message)
        except IndexError or ValueError:
            print("Please enter only numbers and correct TODO!")
            continue

    elif user_action.startswith("exit"):
        print("Bye!")
        break

    else:
        print("You have entered wrong command")