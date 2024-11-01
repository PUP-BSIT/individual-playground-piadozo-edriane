import os




data_record = {

    "name": ["Gerald"],
    "age": ["19"],
    "role_in_class":["President"],
    "major":["Information Technology"],
    "gen_ave":["1.75"],
}


def list_of_dict():

    for key in data_record:
        print (data_record[key])

#DONE
def add_in_dict (range_of_dict):

    os.system('cls')
    for num in range (0, range_of_dict):
        name_of_stud = str(input("Enter the name of the student: "))
        data_record["name"].append(name_of_stud)

        age_of_stud = str(input("Enter the age of the student: "))
        data_record["age"].append(age_of_stud)

        role_of_stud = str(input("Enter the role of the student in classroom: "))
        data_record["role_in_class"].append(role_of_stud)
    
        major_of_stud = str(input("Enter the major of the student: "))
        data_record["major"].append (major_of_stud)

        gen_ave_of_stud = str(input("Enter the general ave of the student: "))
        data_record["gen_ave"].append (gen_ave_of_stud)

#DONE
def update_in_dict ():

    new_info = input("Enter the list (name, age, role, major, average) you want to update: ")
    if new_info in data_record:
        new_value = input (f"Enter the new value for {new_info}: ")
        key_info = int(input("Enter the key index you want to update: "))
        data_record[new_info][key_info] = new_value
    else:
        print ("No data record in dictionary")

    

def delet_in_dict ():
    list_info = input("Enter the list you want to make changes (name, age, role, major, average): ")

    if list_info in data_record:
        remove_data = input("Enter the data you want to remove: ")
        print ("The data is remove")
        data_record[list_info].remove (remove_data)
        
    else:
        print ("No data is available please check List all")


#not yet done
""" 
def search_of_dict():

    search_dict = input("Enter the list (name, age, role, major, average) you want to search for: ")
    search_value = input(f"Enter the search value you want to search in {}")
"""
while True:
    os.system ('cls')
    print ("1. List all")
    print ("2. Add")
    print ("3. Update")
    print ("4. Delete")
    print ("5. Search")
    print ("Exit")

    choice = input("Enter your choice in the menu: ")

    if choice == "Exit" or choice == "exit":
        break

    match choice:
        case "1":
            os.system ('cls')
            print (list_of_dict())
            input("Press enter to continue")

        case "2":
            os.system('cls')

            range_of_dictionary = int(input("How many student information you want to add: "))
            add_in_dict (range_of_dictionary)
            input("Press enter to continue")
        case "3":
            os.system ('cls')
            print (update_in_dict())
            input("Press enter to conitue")
        case "4":
            os.system ('cls')
            print (delet_in_dict())
            input("Press enter to continue")

        case "5":
            print ("Still processing on how can I do it")
        case _:
            os.system ('cls')
            print ("Invalid choice")