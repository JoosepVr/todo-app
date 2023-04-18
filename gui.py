import functions
import PySimpleGUI as Pys
import time

Pys.theme("Dark2")

current_time = Pys.Text("", key="clock")
label = Pys.Text("Type in a to-do")
input_box = Pys.InputText(tooltip="Enter todo", key="todo")
add_button = Pys.Button(size=2, image_source="Add.png", key="Add", tooltip="Add TODO")
list_box = Pys.Listbox(values=functions.get_todos(), key="todos",
					   enable_events=True, size=[45,10])
edit_button = Pys.Button("Edit", tooltip="Edit")
complete_button = Pys.Button("Complete", tooltip="Finish TODO")
exit_button = Pys.Button("Exit")

window = Pys.Window("My To-Do App",
					layout=[[current_time],
							[label],
							[input_box, add_button],
							[list_box, edit_button, complete_button],
							[exit_button]],
					font=("Helvetica", 20))

while True:
	event, values = window.read(timeout=200)
	window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

	if event == "Add":
		todos = functions.get_todos()
		new_todo = values["todo"] + "\n"
		todos.append(new_todo)
		functions.write_todos(todos)
		window["todos"].update(values=todos)

	elif event == "Edit":
		try:
			todo_to_edit = values["todos"][0]
			new_todo = values["todo"]

			todos = functions.get_todos()
			index = todos.index(todo_to_edit)
			todos[index] = new_todo
			functions.write_todos(todos)
			window["todos"].update(values=todos)
		except IndexError:
			Pys.popup("Please select an item first!", font=("Helvetica", 20))
	elif event == "Complete":
		try:
			todo_to_complete = values["todos"][0]
			todos = functions.get_todos()
			todos.remove(todo_to_complete)
			functions.write_todos(todos)
			window["todos"].update(values=todos)
			window["todo"].update("")
			continue
		except IndexError:
			Pys.popup("Please select an item first!", font=("Helvetica", 20))

	elif event == Pys.WIN_CLOSED or event == 'Exit':
		break

	elif event == "todos":
		window["todo"].update(value=values["todos"][0])

window.close()