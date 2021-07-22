# from modules.task_list import *
# print("1st import")
from data.task_list import *
# print("2nd import")
from modules.output import *
# print("3rd import")
from modules.input import *

# print("the begining")
while (True):
    # print("are we here")
    print_menu()
    # option = input("Select an option 1, 2, 3, 4, 5 or (Q)uit: ")
    options()
    print(options())
    if options() == 'q':
        break
    if options() == '1':
        print_list(tasks)
    elif options() == '2':
        print_list(get_uncompleted_tasks(tasks))
    elif options() == '3':
        print_list(get_completed_tasks(tasks))
    elif options() == '4':
        description = input("Enter task description to search for: ")
        task = get_task_with_description(tasks, description)
        if task != "Task Not Found":
            mark_task_complete(task)
    elif options() == '5':
        time = int(input("Enter task duration: "))
        print_list(get_tasks_taking_longer_than(tasks, time))
    elif options() == '6':
        description = input("Enter task description to search for: ")
        print(get_task_with_description(tasks, description))
    elif options() == '7':
        description = input("Enter description: ")
        time_taken = int(input("Enter time taken: "))
        task = create_task(description, time_taken)
        tasks.append(task)
    else:
        print("Invalid Input - choose another option")
