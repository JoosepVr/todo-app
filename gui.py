import functions
import PySimpleGUI as Pys

label = Pys.Text("Type in a to-do")
input_box = Pys.InputText(tooltip="Enter todo")
add_button = Pys.Button("Add")

window = Pys.Window("My To-Do App", layout=[[label, input_box, add_button]])
window.read()
window.close()