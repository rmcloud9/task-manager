while True:
    user_input = input("Type add / show / edit / complete / exit:")

    if 'add' in user_input:
        todo = user_input[4:]

        with open('todos.txt' ,'r') as file:
            todos = file.readlines()
        
        todos.append(todo)

        with open('todos.txt','w') as file:
            file.writelines(todos)

    elif 'show' in user_input:
        with open('todos.txt' ,'r') as file:
            todos = file.readlines()
        # todos = [todo.strip('\n') for todo in todos]       
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}.{item}"
            print(row)

    elif 'edit' in user_input:
        with open('todos.txt' ,'r') as file:
            todos = file.readlines()

        index = int(user_input[5:])
        new_todo = input("Enter the modified todo:")
        todos[index - 1] = new_todo + "\n"

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'complete' in user_input:
        index = int(user_input[9:]) - 1

        with open('todos.txt' ,'r') as file:
            todos = file.readlines()

        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)

        with open('todos.txt','w') as file:
            file.writelines(todos)

        message = f"Todo {todo_to_remove} has been removed from the list."
        print(message)

    elif 'exit' in user_input:
        break

    else:
        print("Invalid command")

print('Goodbye')

