# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 23:10:17 2020

@author: sreek
"""

# Importing necessary packages
import sys
import os
import datetime

# Creating files required
f = open(os.path.join(sys.path[0], "todo.txt"), "a")
done_file = open(os.path.join(sys.path[0], "done.txt"), "a")
f.close()
done_file.close()


# Help function
def help_func():
    print('Usage :-')
    print('$ ./todo add "todo item"  # Add a new todo')
    print('$ ./todo ls               # Show remaining todos')
    print('$ ./todo del NUMBER       # Delete a todo')
    print('$ ./todo done NUMBER      # Complete a todo')
    print('$ ./todo help             # Show usage')
    print('$ ./todo report           # Statistics')


# Function to add a todo item
def add_func(task):
    print('Added todo: "'+task+'"')
    f = open("todo.txt", "a")
    f.write(str(task+"\n"))
    f.close()


# Display list of todos
def ls_func():
    f = open("todo.txt", "r")
    f.seek(0)
    task_list = (f.readlines())
    f.close()
    if len(task_list) == 0:
        # if no remaining todos
        print("There are no pending todos!")
    else:
        # loop through the array and display
        for i in range(len(task_list)-1, -1, -1):
            print(str('['+str(i+1)+']'), task_list[i][:-1])


# Delete function
def del_func(num):
    f = open("todo.txt", "r")
    temp_arr = f.readlines()
    f.close()
    if (num > len(temp_arr)) or (num < 1):
        # If todo number does not exist or if an invalid number is entered
        print("Error: todo #"+str(num)+" does not exist. Nothing deleted.")
    else:
        # finds index value and deletes it
        temp_arr.pop(num-1)
        print("Deleted todo #"+str(num))
        f = open("todo.txt", "w")
        # Update the todo file
        f.writelines(temp_arr)


# Done function
def done_func(num):
    f = open("todo.txt", "r")
    temp_arr = f.readlines()
    f.close()
    if (num > len(temp_arr)) or (num < 1):
        # If todo number does not exist or if an invalid number is entered
        print("Error: todo #"+str(num)+" does not exist.")
    else:
        # finds index value and pops it out
        done_item = temp_arr.pop(num-1)[:-1]
        print("Marked todo #"+str(num)+" as done.")
        # Update the todo file
        f = open("todo.txt", "w")
        f.writelines(temp_arr)
        # Finding date
        x = datetime.datetime.now()
        date_val = str(x.strftime("%Y")+"-"+x.strftime("%m")+"-"+x.strftime("%d"))
        # The todo is concatenated to form a string as per requirement
        write_obj = str("x "+date_val+" "+done_item)
        done_file = open("done.txt", "a")
        done_file.seek(0)
        # Done file is updated
        done_file.write(str(write_obj+"\n"))
        done_file.close()


# report function
def report_func():
    todo_file = open("todo.txt", "r")
    done_file = open("done.txt", "r")
    x = datetime.datetime.now()
    # Finding current date
    date_val = str(x.strftime("%Y")+"-"+x.strftime("%m")+"-"+x.strftime("%d"))
    # Number of tasks are found using length of respective files
    pending_ctr = len(todo_file.readlines())
    done_ctr = len(done_file.readlines())
    print(date_val, "Pending :", pending_ctr, "Completed :", done_ctr)

    
# Driver code
if len(sys.argv) > 1:
    # checks for any command line argument and runs corresponding function
    if sys.argv[1] == 'help':
        help_func()
    elif sys.argv[1] == 'add':
        if len(sys.argv) == 2:
            # todo argument is not found
            print("Error: Missing todo string. Nothing added!")
        else:
            add_func(str(sys.argv[2]))
    elif sys.argv[1] == 'ls':
        ls_func()
    elif sys.argv[1] == 'del':
        if len(sys.argv) == 2:
            # Number argument is not found
            print("Error: Missing NUMBER for deleting todo.")
        else:
            del_func(int(sys.argv[2]))
    elif sys.argv[1] == 'done':
        if len(sys.argv) == 2:
            # Number argument is not given
            print("Error: Missing NUMBER for marking todo as done.")
        else:
            done_func(int(sys.argv[2]))
    elif sys.argv[1] == 'report':
        report_func()

else:
    help_func()


