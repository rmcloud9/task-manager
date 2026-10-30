def get_todos(filepath='todos.txt'):
    """Read the text file and 
    return the list of to-do items.
    """
    with open(filepath ,'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(new_todos, filepath='todos.txt'):
    """Write the to-do items list in a text file"""
    with open(filepath,'w') as file:
        file.writelines(new_todos)
