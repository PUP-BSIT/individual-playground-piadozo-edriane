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


    for num in range (0, range_of_dict):
        name_of_stud = str(input("Enter the name of the student: "))
        data_record["name"].append(name_of_stud)

        age_of_stud = int(input("Enter the age of the student: "))
        data_record["age"].append(age_of_stud)

        role_of_stud = str(input("Enter the role of the student in classroom: "))
        data_record["role_in_class"].append(role_of_stud)
    
        major_of_stud = str(input("Enter the major of the student: "))
        data_record["major"].append (major_of_stud)

        gen_ave_of_stud = int(input("Enter the general ave of the student: "))
        data_record["gen_ave"].append (gen_ave_of_stud)

#DONE
def update_in_dict (range_of_dict):

    new_info = str (input("Enter the list name you want to update: "))
    for num in range (0, range_of_dict):
    
        if new_info == "name":
            update_name = str(input("Enter the name you want to update: "))
            data_record["name"].append (update_name)
        elif new_info == "age":
            update_age = str(input("Enter the age you want to update: "))
            data_record["age"].append (update_age)
        elif new_info == "role":
            update_role = str(input("Enter the role you want to update"))
            data_record["role_in_class"].append(update_role)
        elif new_info == "major":
            update_major = str(input("Enter the major you want to update: "))
            data_record["major"].append (update_major)
        elif new_info == "ave":
            update_ave = str(input("Enter the avergage you want to update: "))
            data_record["gen_ave"].append (update_ave)
        else:
            print ("No list in the dictionary")

#not yet done
def search_of_dict():

    search_name = int(input("Enter the number you want to find: "))
    for key in data_record:
        if isinstance (data_record["name"], list):
            print (data_record["name"])
        else:
            print ("There's no record")


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
            input("Press enter to")
        case "3":
            os.system ('cls')
            range_of_dictionary = int(input("Enter the range of the dictionary: "))
            print (update_in_dict(range_of_dictionary))

        case _:
            os.system ('cls')
            print ("Invalid choice")