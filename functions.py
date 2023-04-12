FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH): # filepath gets the  file.
    """ Reads a text file and returns the list to-do items """
    with open(filepath, "r") as file_local:  # "r" reads.
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """ Writes in a text file. """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")