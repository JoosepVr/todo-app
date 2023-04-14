import functions
import PySimpleGUI as Pys

label = Pys.Text("Type in a to-do")
input_box = Pys.InputText(tooltip="Enter todo", key="todo")
add_button = Pys.Button("Add")
list_box = Pys.Listbox(values=functions.get_todos(), key="todos",
					   enable_events=True, size=[45,10])
edit_button = Pys.Button("Edit")

window = Pys.Window("My To-Do App",
					layout=[[label], [input_box, add_button], [list_box, edit_button]],
					font=("Helvetica", 20))

while True:
	event, values = window.read()
	print(1, event)
	print(2, values)

	if event == "Add":
		todos = functions.get_todos()
		new_todo = values["todo"] + "\n"
		todos.append(new_todo)
		functions.write_todos(todos)
		window["todos"].update(values=todos)
	elif event == "Edit":
		todo_to_edit = values["todos"][0]
		new_todo = values["todo"]

		todos = functions.get_todos()
		index = todos.index(todo_to_edit)
		todos[index] = new_todo
		functions.write_todos(todos)
		window["todos"].update(values=todos)
	elif event == "todos":
		window["todo"].update(value=values["todos"][0])
	elif event == Pys.WIN_CLOSED:
		break

window.close()