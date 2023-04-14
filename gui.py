import functions
import PySimpleGUI as Pys

label = Pys.Text("Type in a to-do")
input_box = Pys.InputText(tooltip="Enter todo", key="todo")
add_button = Pys.Button("Add")

window = Pys.Window("My To-Do App",
					layout=[[label], [input_box, add_button]],
					font=("Helvetica", 20))

while True:
	event, values = window.read()
	print(event)
	print(values)
	if event == "Add":
		todos = functions.get_todos()
		new_todo = values["todo"] + "\n"
		todos.append(new_todo)
		functions.write_todos(todos)
	elif event == Pys.WIN_CLOSED:
		break

window.close()