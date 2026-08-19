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

while True:
    user_input = input("Type add / show / edit / complete / exit:")

    if user_input.startswith('add'):
        todo = user_input[4:]

        todos = get_todos()
        
        todos.append(todo + '\n')

        write_todos(todos)

    elif user_input.startswith('show'):
        todos = get_todos()
        # todos = [todo.strip('\n') for todo in todos]  can use list comprehension in code     
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}.{item}"
            print(row)

    elif user_input.startswith('edit'):
        try:    
            index = int(user_input[5:])

        except ValueError:
            print("Invalid input format")
            continue

        todos = get_todos()

        index = index - 1
        new_todo = input("Enter the modified todo:")
        todos[index] = new_todo + "\n"
        
        write_todos(todos)

    elif user_input.startswith('complete'):
        try:
            index = int(user_input[9:]) - 1

            todos = get_todos()

            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo {todo_to_remove} has been removed from the list."
            print(message)

        except IndexError:
            print("Index entered does not exist")
            continue

        except ValueError:
            print("Invalid input format")
            continue

    elif user_input.startswith('exit'):
        break

    else:
        print("Invalid command")

print('Goodbye')
