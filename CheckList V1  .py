from time import sleep as s
from os import system, name

obj_list = []  # List where code is transferred to from ".txt" file

def clear():
    if name == 'nt':
        _ = system('cls')
    else:                 
        _ = system('clear')

numbers = [str(i) for i in range(1, 31)]
x = 0
y = 0
xrx = 0

# Reading data from .txt file to convert to list to show
with open("CLV1.txt", 'r') as file: 
    content = file.read()

xrx = content.count("|")

# Initializing obj_list with empty strings based on count of "|" then adds all attributes to list
obj_list = [""] * xrx
for char in content:
    if char != "|":
        obj_list[y] += char
    else:
        y += 1

# Saves list to text file function
def save_to_file():
    with open("CLV1.txt", 'w') as file: 
        v11 = "|".join(obj_list) + "|"
        file.write(v11)

while True:
    clear()
    if len(obj_list) != 1 and obj_list[0] == "Nothing In List!":
        obj_list.pop(0)

    save_to_file()

    for idx, task in enumerate(obj_list):
        if task == "":
            break
        else:
            print(f"{idx + 1}. {task}")

    print("\n\n")
    main_choice = input("""[a]dd / [r]emove a task or move task to [t]op / [b]ottom or [s]witch two - - - >  """)

    if main_choice.lower() == "r":
        rc = input("\nEnter the number of the task you want to remove - - - >  ")
        if rc in numbers:
            rc = int(rc) - 1
            obj_list.pop(rc)
            if len(obj_list) == 0:
                obj_list.append("Nothing In List!")
        else:
            print("Not Valid Input!")
        
    elif main_choice.lower() == "t":
        tc = input("\nEnter the number of the task you want to move to the top - - - >  ")
        if tc in numbers:
            tc = int(tc) - 1
            obj_list.insert(0, obj_list.pop(tc))
        else:
            print("Not Valid Input!")
       
    elif main_choice.lower() == "b":
        bc = input("\nEnter the number of the task you want to move to the bottom - - - >  ")
        if bc in numbers:
            bc = int(bc) - 1
            obj_list.append(obj_list.pop(bc))
        else:
            print("Not Valid Input!")

    elif main_choice.lower() == "a":
        ac = input("\nEnter the task you would like to add to the list - - - >  ")
        obj_list.append(ac)

    elif main_choice.lower() == "s":
        s1 = input("Enter the first attribute you want to switch - - - >  ")
        s2 = input("Enter the second attribute you want to switch - - - >  ")
        if s1 in numbers and s2 in numbers:
            s1, s2 = int(s1) - 1, int(s2) - 1
            obj_list[s1], obj_list[s2] = obj_list[s2], obj_list[s1]
        else:
            print("Not Valid Input!")
        
    else:
        pass