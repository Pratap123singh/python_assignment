# 3. Write a menu driven program to practice Dictionary functions.
# Write a program to accept name of a person and their vehicle and store it in a dictionary.
# Ask user if they want to continue to accept multiple values.
# Display following menu:
# a. Add new person name and a vehicle name.
# b. Delete a person name and vehicle name from the dictionary.
# ----Accept person name from user.
# ----Check whether person name exists in the dictionary.
# ----If exists show person name and vehicle name to the user.
# ----Confirm for deletion, if user enters y
# then delete otherwise no. Display appropriate message.
# c. Modify vehicle name for the person
# ----Accept a person name from user.
# ----Check whether the person’s name exists.
# ----If the name exists, show the person’s name and vehicle name to user.
# Ask for new value and then overwrite the old value.
# d. Search vehicle for the given person’s name.
# e. Search list of people, who have given a vehicle
# f. Display all person names.
# g. Display all vehicle names.
# h. Exit
d={'Paras': 'BMW', 'Yulia': 'Mercedes', 'Rahul': ''}
_quit=0

def _1(d: dict):
    _name=input("Enter vehicle owner name: ")
    _vehicle_name=input("Enter vehicle name: ")
    d[_name]=_vehicle_name
    return d

def _2(d: dict, name: str):
    del d[name]
    print(d)

def _3(d: dict, owner_name: str, vehicle_name_update: str):
    d[owner_name] = vehicle_name_update
    return d

def _4(d: dict, owner_vehicle_search: str):
    for k,v in d.items():
        if k == owner_vehicle_search:
            print(k ,":", d[k])

def _5(d: dict):
    r = {k:v for k,v in d.items() if v != ''}
    return r

def _6(d: dict):
    name={k for k in d.keys()}
    print("\n")
    return name

def _7(d: dict):
    vehicle_name=[v for v in d.values()]
    return vehicle_name

while _quit != 'q':
    print("\n")
    print("Add new person name and a vehicle name. Press 1")
    print("Delete a person name and vehicle name from the dictionary. Press 2")
    print("Modify vehicle name for the person. Press 3")
    print("Search vehicle for the given person name. Press 4")
    print("Search list of people, who have given a vehicle. Press 5")
    print("Display all person names. Press 6")
    print("Display all vehicle names. Press 7")
    print("Exit. Press 8")
    print("\nEnter your choice: ", end="")
    _user_choice=int(input())

    if _user_choice == 1:
        _1(d)
    if _user_choice == 2:
        name=input("Enter owner name to be deleted: ")
        _2(d, name)
    if _user_choice == 3:
        name=input("Enter owner name whose vehicle to update: ")
        vehicle_name_update=input("Enter new vehicle name: ")
        print(_3(d, name, vehicle_name_update))
    if _user_choice == 4:
        owner_vehicle_search=input("Enter vehicle name to be searched: ")
        _4(d,owner_vehicle_search)
    if _user_choice == 5:
        print(_5(d))
    if _user_choice == 6:
        print(_6(d))
    if _user_choice == 7:
        print(_7(d))
    if _user_choice == 8:
        _quit = 'q'
