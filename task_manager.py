while True:
    user_input = input("Type add / show / edit / complete / exit:")

    if user_input.startswith('add'):
        todo = user_input[4:]

        with open('todos.txt' ,'r') as file:
            todos = file.readlines()
        
        todos.append(todo + '\n')

        with open('todos.txt','w') as file:
            file.writelines(todos)

    elif user_input.startswith('show'):
        with open('todos.txt' ,'r') as file:
            todos = file.readlines()
        # todos = [todo.strip('\n') for todo in todos]       
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

        with open('todos.txt' ,'r') as file:
            todos = file.readlines()

        index = index - 1
        new_todo = input("Enter the modified todo:")
        todos[index] = new_todo + "\n"
        
        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_input.startswith('complete'):
        try:
            index = int(user_input[9:]) - 1

            with open('todos.txt' ,'r') as file:
                todos = file.readlines()

            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt','w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} has been removed from the list."
            print(message)

        except IndexError:
            print("Index entered does not exist")
            continue

    elif user_input.startswith('exit'):
        break

    else:
        print("Invalid command")

print('Goodbye')

