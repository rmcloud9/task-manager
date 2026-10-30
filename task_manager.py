import functions

while True:
    user_input = input("Type add / show / edit / complete / exit:")

    if user_input.startswith('add'):
        todo = user_input[4:]

        todos = functions.get_todos()
        
        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_input.startswith('show'):
        todos = functions.get_todos()
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

        todos = functions.get_todos()

        index = index - 1
        new_todo = input("Enter the modified todo:")
        todos[index] = new_todo + "\n"
        
        functions.write_todos(todos)

    elif user_input.startswith('complete'):
        try:
            index = int(user_input[9:]) - 1

            todos = functions.get_todos()

            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

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