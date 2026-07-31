while True:
    user_input = input("Type add / show / edit / complete / exit:")

    match user_input:
        case 'add':
            todo = input("Enter a new todo:") + "\n"
            file = open('todos.txt' , 'r')
            todos = file.readlines()
            file.close()
            todos.append(todo)
            file = open('todos.txt' , 'w')
            todos = file.writelines(todos)
            file.close()

        case 'show':
            file = open('todos.txt' , 'r')
            todos = file.readlines()
            file.close()
            for index, item in enumerate(todos):
                row = f"{index + 1}.{item}"
                print(row)

        case 'edit':
            index = int(input("Enter the serial number of todo you want to edit:"))
            new_todo = input("Enter the modified todo:")
            todos[index - 1] = new_todo

        case 'complete':
            index = int(input("Enter the serial number of todo you want to complete:"))
            todos.pop(index - 1)

        case 'exit':
            break

print('Goodbye')

