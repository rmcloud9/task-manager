while True:
    user_input = input("Type add / show / edit / complete / exit:")

    match user_input:
        case 'add':
            todo = input("Enter a new todo:") + "\n"

            with open('todos.txt' ,'r') as file:
                todos = file.readlines()
            
            todos.append(todo)

            with open('todos.txt','w') as file:
                file.writelines(todos)

        case 'show':
            with open('todos.txt' ,'r') as file:
                todos = file.readlines()
            # todos = [todo.strip('\n') for todo in todos]       
            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}.{item}"
                print(row)

        case 'edit':
            with open('todos.txt' ,'r') as file:
                todos = file.readlines()

            index = int(input("Enter the serial number of todo you want to edit:"))
            new_todo = input("Enter the modified todo:")
            todos[index - 1] = new_todo + "\n"

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("Enter the serial number of todo you want to complete:"))
            index = number - 1

            with open('todos.txt' ,'r') as file:
                todos = file.readlines()

            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt','w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} has been removed from the list."
            print(message)

        case 'exit':
            break

print('Goodbye')

