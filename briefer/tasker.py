# todoer 0.1.1-5 - complete 29.10.24
#
# program which records & displays goals
#
# will hold the : date of creation [x]
#
# description of goal [x]
#
# title of goal [x]
#
# write to file [x]
#
# display from file [x]
#
# 0.1.5-8 - complete 29.10.24
#
# edit tasks [x]
#
# convert to JSON format [x]
#
#
# # 0.1.9 - complete 29.10.24
# 
# check tasks off as completed [x] 
#
# clean-up spacing [x] 
#



# ************
# ******
# ***
#
# 0.2.0 -
#
# Multi-delete [ ] 
#
# Integrate view_tasks to intro window [x]
#
# Rearrange Exit vs Complete [ ]
#
# 0.2.1 -
#
# Integrate with briefer [x]
# 
# 
#
# 0.2.2 - 
#
# Order tasks completed at top [ ]
#
#
# Integrate with logger [ ]
#
# 
#
# Introduce subtasks [ ]
#
# Change created_at to countup [ ]
#
# Introduce target_date as countdown [ ]
#
#
#
#




version = '0.1.9'

import json

import os, time
from datetime import datetime 

TODO_FILE = 'todo.json'

def init_json_file():
    
    if not os.path.exists(TODO_FILE) or os.path.getsize(TODO_FILE) == 0: 
        with open(TODO_FILE, 'w') as file:
            json.dump([], file)


def load_tasks():
    try:
        with open(TODO_FILE, 'r') as file:
            return json.load(file)

    except json.JSONDecodeError:
        print('Error reading JSON File. Attempting correction...')
        with open(TODO_FILE, 'w') as file:
            json.dump([], file)
        return []
    except FileNotFoundError:
        return [] 



def add_task(task, description =''):

    tasks = load_tasks()


    task_entry = {

        "title": task,
        "description": description,
        "created_at": datetime.now().strftime('%Y-%d-%m %H:%M'),
        "completed": False,
        "completed_at": None
    }

    tasks.append(task_entry)
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent =4)
    print('Task added: {}'.format(task))




def complete_task(task_num):
    tasks = load_tasks()

    try:
        task = tasks[task_num - 1]
        
        task["completed"] = not task["completed"]
        
        task["completed_at"] = datetime.now().strftime('%Y-%d-%m %H:%M')

        with open(TODO_FILE, 'w') as file:

            json.dump(tasks, file, indent=4)

        status = "completed" if task["completed"] else "incomplete"

        print("Task marked as {}: {}".format(status, task['title']))

    except IndexError:
        print('Task number out of range.')

    




def view_tasks():

    tasks = load_tasks()

    print('Your tasks: ')
    if not tasks:
        print('No tasks found. Add some tasks!')
        
    for index, task in enumerate(tasks, start=1):
        status = "[ ]" if not task["completed"] else "[x]" 
        print(f"{index}. {task['title']} {status}")
        if task["description"]:
            print(f"Notes:  {task['description']}\n")
        print(f"Created: {task['created_at']}\n")
        
        

            



    


        


def edit_task(task_num):



        tasks = load_tasks()

        
        try:
            task = tasks[task_num - 1]
            print('Current task: {}'.format(task['title']))
            print('Current notes: {}'.format(task['description']))
            print('Created at: {}'.format(task['created_at']))

            new_task = input('Edit title or press enter to cancel..')
            new_description = input('Enter new notes or press enter to cancel..')

            task["title"] = new_task or task["title"]
            task["description"] = new_description or task["description"]



            with open(TODO_FILE, 'w') as file:
                json.dump(tasks, file, indent = 4) 

            print('Task update successful.')

            
        except IndexError:
            print('Task number out of range.')







def del_task(task_num):

        tasks = load_tasks()


        try:
            removed_task = tasks.pop(task_num - 1)

            with open(TODO_FILE, 'w') as file:
                json.dump(tasks, file, indent=4)
            print('Task removed: {}'.format(removed_task['title']))

        except IndexError:
            print('Task number out of range.')


















def main():

    init_json_file()

    t = 0.035


    print('\nWelcome to Tasker, version {}\n'.format(version))
    time.sleep(1)

    view_tasks()
    
    while True:



        

        print('\n1. Add Tasks')
        time.sleep(t)
        print('2. Edit Tasks')
        time.sleep(t)
        print('3. View Tasks')
        time.sleep(t)
        print('4. Delete Tasks')
        time.sleep(t)
        print('5. Complete Tasks')
        time.sleep(t)
        print('6. Exit Tasker')

        init = False

        reply = input('..')



        

        if reply == '1':
            task = input('What objective would you like to record? .. ')
            description = input('Enter any notes, or press enter to skip .. ')
            add_task(task, description)

        elif reply == '2':
            task_num = int(input('Which number task to edit? .. '))
            edit_task(task_num)
            

        elif reply == '3':
            view_tasks()

            
        elif reply == '4':
            task_num = int(input('Which number task to delete? .. '))
            del_task(task_num)


        elif reply =='5':
            time.sleep(t)
            task_num = int(input('Which task have you completed? .. '))
            complete_task(task_num)

                           
        elif reply == '6':
            time.sleep(0.5)
            print('Goodbye!')
            time.sleep(0.5)
            break

        
                           

        else:
            print('Unrecognised input.')






if __name__ == '__main__':
    main()



'''
get_note = 'None'

print('Target completion date in Format = ')
get_date=input('//')
print('Would you like to add any further notes?')
reply = input('..').upper()
if reply == 'Y':
    print('Very good, sir. Initiating note record : ')
    get_note = input('``')



print(get_goal, get_date, get_note)
'''




