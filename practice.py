import os
from math import sqrt
import re
import operator

#KEEP GOING, AND PRACTICE ANY PROBLEM YOU WANT !
"""
os.system('cls')
print ("1. Grades computer")
print ("2. The number that closest to 100")
print ("3. Circumference of circle")
print ("4. Absolute difference")
print ("5. String manipulation")
choice = input("Enter your choice in the number of problem: ")

match choice:
    case "1":
        os.system('cls')
        prelims = int(input("Enter your prelims grade: "))
        midterm = int (input("Enter your midterm grades: " ))
        finals = int (input("Enter your finals grades: "))
        average = (prelims + midterm + finals) / 3 

        if average > 96:
            print ("Your equivalent grade is: 1.00")
        elif average <= 96 and average >= 94:
            print ("Your equivalent grade is: 1.25")
        elif average <= 93 and average >= 91:
            print ("Your equivalent grade is: 1.50")
        elif average <= 90 and average >= 88:
            print ("Your equivalent grade is: 1.75")
        elif average <= 87 and average >= 85:
            print ("Your equivalent grade is: 2.00 ")
        elif average <= 84 and average >= 82:
            print ("Your equivalent grade is: 2.25")
        elif average <= 81 and average >= 78:
            print ("Your equivalent grade is: 2.50")
        elif average <= 77 and average >= 75:
            print ("Your equivalent average is: 2.75")
        elif average == 75:
            print ("Your equivalent grade is: 3.00")
        else:
            print ("Your equivalent grade is: 5.00")

    case "2":
        os.system('cls')
        num_one = int (input("Enter the first number: "))
        num_two = int (input ("Enter the second number: "))

        absolute_value_one = abs(num_one - 100)
        absoulute_value_two = abs(num_two - 100)

        if absolute_value_one <= 100 and absolute_value_one > absoulute_value_two:
            print (f"The first number is the closest to 100 whicih is the number: {absolute_value_one}")
        elif absoulute_value_two <= 100 and absoulute_value_two > absolute_value_one:
            print (f"The second number is the closest number in 100 which is the number: {absoulute_value_two}")
        else:
            print ("Both are equal") 
    case "3":
        os.system ('cls')
        radius = int (input ("Enter the radius of the circle: "))

        circumference = 2 * 3.14 * radius

        print (f"The cricumference of the cricle is: {circumference}")
    case "4":
        os.system('cls')
        num_abs = int(input("Enter a number: "))
        absoulute_value = abs (num_abs)

        print (f"The absolute value of the number is: {absoulute_value}")
    case "5":
        os.system('cls')
        word = input("Enter a 5 char word: ")

        
        word = word[0: len(word)-2]

        print (f"The word is: {word}")

    case _:
            print ("Input the correspanding number of the problem")
"""

"""
os.system('cls')

#KEEP GOING, AND PRACTICE ANY PROBLEM YOU WANT !
print ("1. Input to the list")
print ("2. Sum of the list")
print ("3. Greatest number in the list")
print ("4. Even number in the list")
print ("5. Descending list")


choice = input ("Enter the number of the problem you want to solve: ")

match choice: 

    case "1":
        os.system('cls')
        list_1 = []
        range_of_list1 = int(input("Enter the range of the list: "))
        for i in range (1, range_of_list1):
            ele_of_list1 = int(input("Enter the element of the list: "))
            list_1.append (ele_of_list1)
        print (f"The elements of the list{list_1}")
    case "2":
        os.system('cls')
        list_2 = []
        sum_of_list = 0
        range_of_list2 = int (input("Enter the range of the list: "))

        for i in range (1, range_of_list2):
            ele_of_list2 = int(input("Enter the elements in the list: "))
            list_2.append (ele_of_list2)
        for i in range (1, range_of_list2):
            sum_of_list = sum(list_2)

        print (f"The sum of the list: {sum_of_list}")   
        
    case "3":
        os.system('cls')
        list_3 = []

        range_of_list3 = int(input("Enter the range of the list: "))

        for i in range (1, range_of_list3):
            ele_of_list3 = int(input("Enter the element of the list: "))
            list_3.append (ele_of_list3)
            greatest_num_lis = max(list_3)
        print (f"The greatest element in the list: {greatest_num_lis}")
    case "4":
        os.system ('cls')
        list_4 = []
        range_of_list4 = int(input("Enter the range of the list: "))
        
        for i in range (1, range_of_list4):
            ele_of_list4 = int(input("Enter the element of the list: "))
            list_4.append (ele_of_list4)
      
        if list_4 %2 == 1:
            print ("The odd number of the list: {list_4}")

    case _:
        print ("Invalid choice")
    """

os.system('cls')

#1. a function that accepts the list as an input and returns the sum of the list
#2. a function that accepts the list as an input and returns the average of the items
#3. a function that accepts the list as an input and returns the highest value
#4. a function that returns the factorial of the number
#5. a function that accepts the input and return whethere the number is prime or not
"""
list_1 = []
list_2 = []
list_3 = []
list_5 = []

def sum_of_list (range_of_list_1):
    total = 0
    for num in range (0, range_of_list_1):
        ele_of_list_1 = int(input("Enter the elements on the list: "))
        list_1.append (ele_of_list_1)
    
    for num in list_1:
        total = num + total
    return total

def average_of_list (range_of_list_2):
    total_sum_2 = 0
    total_ave_list = 0
    for num in range (0, range_of_list_2):
        ele_of_list_2 = int(input("Enter the elements of the list: "))
        list_2.append (ele_of_list_2)
    
    for num in list_2:
        total_sum_2 = num + total_sum_2
    
    total_ave_list = total_sum_2 / len(list_2)

    return total_ave_list

def highest_value (range_of_list_3):

    for num in range (0, range_of_list_3):
        ele_of_list_3 = int(input("Enter the elements in the array: "))
        list_3.append(ele_of_list_3)

    for num in range (0, range_of_list_3):
        greatest_num_list = max(list_3)

    return greatest_num_list

def factorial_num (nums):
    factorial_num = 1

    for num in range (1, nums + 1):

        factorial_num = num * factorial_num

    return factorial_num
    
def prime_or_composite (nums):
    if nums <= 1:
        print ("It's not a prime number")
        return False
    for num in range (2, int(sqrt(nums)) + 1):
            if nums % num == 0:
                print ("It's not a prime number")
                return False
            else:
                print ("It's a prime number")
                return True
    else:
        print ("It's a prime number")
        return True
      





while True:
    os.system ('cls')
    print ("1. A function that returns the sum of the list")
    print ("2. A function that returns the average of the items")
    print ("3. A function that returns the highest value in the list")
    print ("4. A function that returns the factorial of the number")
    print ("5. A function that Identify the number if it's prime or not and returns the value")
    print ("Type quit or Quit to exit the program")

    choice = input("Enter the choice of the problem: ")
    if choice == "Quit" or choice == "quit":
        print ("The menu will exit")
        break

    match choice:
        case "1":
            os.system('cls')
            range_list_1 = int(input("Enter the range of the list: "))
            print (f"The sum of the list: {sum_of_list (range_list_1)}")
            input ("Press enter to continue to another problem")

        case "2":
            os.system ('cls')
            range_list_2 = int(input("Enter the range of the list: "))
            print (f"The total average of the array: {average_of_list(range_list_2)}")
            input ("Press enter to continue to another problem")

        case "3":
            os.system ('cls')
            range_list_3 = int(input("Enter the range of the list: "))
            print (f"The highest number in the array: {highest_value(range_list_3)}")
            input ("Press enter to continue to another problem")

        case "4":
            os.system('cls')
            num = int(input("Enter a number: "))
            print (f"The factorial number of the list: {factorial_num(num)}")
            input ("Press enter to continue to another problem")

        case "5":

            os.system ('cls')
            num = int (input("Enter a number: "))
            print (prime_or_composite(num))
            input ("Press enter to continue to another problem")

        case _:
            print ("Invalid input of number")
"""
"""
list_test = []

def even_odd (range_of_list_1):
    for num in range (0, range_of_list_1):
        ele_of_list = int(input("Enter the element of list: "))
        list_test.append (ele_of_list)

    for num in range (0, range_of_list_1):
        value = list_test[num]
        if value %2 == 0:
            print (f"The even number in list: {value} in the index number of: {num}")
        else:
            print (f"The odd number in the list: {value} in the index number of: {num}")

range_of_list_1 = int(input("Enter the range of the list: "))
even_odd(range_of_list_1)
"""
"""
os.system('cls')
responese_data = {
    "status code" : 200,
    "Name": [],
    "cities":{
        "Philippines": "Manila"
    },   
}


countries_input = int(input("Enter the number of country you will input: "))

for num in range (0, countries_input):
    countries = str(input("Enter the countries: "))
    responese_data["Name"].append (countries)

print (responese_data["Name"])

"""
""" 
list_of_all = []

def descending_list (range_of_num):
    
    for num in range (0, range_of_num):
        ele_of_list = int(input("Enter a number: "))
        list_of_all.append (ele_of_list)

    for num in range (range_of_num - 1, -1, -1):
        print (f"The descending form of array: {list_of_all[num]}")
        
        
def rev_string (word):
    string_word = list(word)

    for num in range (len(string_word) -1, -1, -1): # manual descending sequence
        print (string_word[num], end="")

def occu_of_letter (word):
    string_word = list(word.upper())
    total_occur = 0
    letter_finder = str(input("Enter the letter you want to find: "))

    for num in range (len(string_word)):
        if letter_finder == string_word[num]:
            total_occur = total_occur + 1
    print (f"The total occurance of letter {letter_finder} is : {total_occur}")

def occu_of_number (range_of_list):
    total_occur_num = 0

    num_finder = int(input("Enter the number you want to find: "))

    for num in range (0, range_of_list):
        ele_of_list = int(input("Enter the element of the list: "))
        list_of_all.append(ele_of_list)

    for num in range (0, range_of_list):
        if num_finder == list_of_all[num]:
            total_occur_num = total_occur_num + 1
    
    print (f"The total occurance of the number: {total_occur_num}")

def palindrome (word):
    string_word = word.upper()
    
    if string_word == string_word [::-1]:# descending sequence
            print ("It's a palindrome")
    else:
            print ("It's not a palindrome")

os.system('cls')
print ("1. Descending List")
print ("2. Reverse string")
print ("3. Occurance of letter")
print ("4. Occurance of number")
print ("5. Palindrome string")

choice = int(input("Enter the number of the problem: "))

match choice:
    case 1:
        os.system('cls')
        range_of_num = int(input("Enter thr range of the list: "))
        descending_list (range_of_num)
    case 2:
        os.system('cls')
        word = str(input("Enter a word: "))
        rev_string (word)
    case 3:
        os.system('cls')
        word = str(input("Enter a word: "))
        occu_of_letter (word)
    case 4:
        os.system('cls')
        range_of_num = int(input("Enter the range of the list: "))
        occu_of_number (range_of_num)

    case 5:
        os.system('cls')
        word = str(input("Enter a word:"))
        palindrome (word)
    case _:
        print ("Invalid choice")
"""
"""
def add (*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print (add(1,2,3,4,5))
"""
"""
dict = {
 "message": ["Hello wordl!", "Edriane"],
 "language": "english",
 "response": "Hi there!",
}
dict_key = int(input("Enter the number you want to replace: "))
for key in dict:
  
    if isinstance(dict[key], list):
        print (dict[key][dict_key])
"""

""" 
list_of_all = []


def mult_table (num_to_mult, range_of_loop):
    multiple_table = 0

    print ("The multiplcation table")
    for num in range (1, range_of_loop):
        multiple_table = num * num_to_mult
        print (f"{num_to_mult} * {num} = {multiple_table}")

    return " "
    
def swap_ele (range_of_list):
    
    for num in range (0, range_of_list):
        ele_of_list = int(input("Enter the element of the list: "))
        list_of_all.append(ele_of_list)
    
    print (f"The current list: {list_of_all}")
  
    swap_1 = int(input("Enter the index first index value you want to swap: "))
    swap_2 = int(input("Enter the index value you want to swap to: "))
   
    list_of_all[swap_1], list_of_all[swap_2] = list_of_all[swap_2], list_of_all[swap_1]

    print (f"The swapped list: {list_of_all}")
    
    return " "
 
def min_list(range_of_list):

    for num in range (0, range_of_list):
        ele_of_list = int(input("Enter the element of list: "))
        list_of_all.append(ele_of_list)
        min_of_list = min(list_of_all)

    print (f"The minimun number in list is: {min_of_list}")
    
    return " "

def count_eve_odd (range_of_list):
    even_counter = 0
    odd_counter = 0

    for num in range (0, range_of_list):
        ele_of_list = int(input("Enter the element in the list: "))
        list_of_all.append(ele_of_list)

        if list_of_all[num] %2 == 0:
            even_counter = even_counter + 1
        else:
            odd_counter = odd_counter + 1

    print (f"The occurance of even number in the list: {even_counter}")
    print (f"The occurance of odd number in the list: {odd_counter}")

    return " "


def sum_eve_odd (range_of_list):
    sum_of_even = 0
    sum_of_odd = 0

    for num in range (0, range_of_list):
        ele_of_list = int(input("Enter the elements in the list: "))
        list_of_all.append(ele_of_list)
       

    even_numbers =[num for num in list_of_all if num %2 == 0]
    sum_of_even = sum(even_numbers)

    odd_numbers = [num for num in list_of_all if num %2 == 1]
    sum_of_odd = sum(odd_numbers)

    print (f"The sum of even number in list: {sum_of_even}")
    print (f"The sum of odd number in the list: {sum_of_odd}")
    return "    "


while True:
    print ("1. Multiplication Table: ")
    print ("2. Swap two elements in a list")
    print ("3. Least number in the list")
    print ("4. Count even and Odd")
    print ("5. Sum of even in list")
    print ("Exit")

    choice = input("Enter the number of the problem: ")

    if choice == "Exit" or choice == "exit":
        break

    match choice:
        case "1":
            os.system ('cls')   
            num_to_mult = int(input("Enter the number you want to multiply: "))
            range_of_num = int(input("Enter the range of the number you want to multiply: "))
            print (mult_table(num_to_mult, range_of_num))
        case "2":
            os.system('cls')
            range_of_list = int(input("Enter the range of list: "))
            print(swap_ele(range_of_list))
        case "3":
            os.system('cls')
            range_of_list = int(input("Enter the range of list: "))
            print (min_list(range_of_list))
        case "4":
            os.system('cls')
            range_of_list = int(input("Enter the range of the list: "))
            print(count_eve_odd(range_of_list))

        case "5":
            os.system('cls')
            range_of_list = int(input("Enter the range of the list: "))
            print(sum_eve_odd(range_of_list))
        case _:
            print ("Invalid input")
"""
""" 
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1, 2, 3, 4, 5))
print(add(7, 4, 3))
print(add(1, 3, 4, 5))
"""
""" 
def calculate(**kwargs):
    print(kwargs)

calculate(num_1=3, num_2=5, operator="+")

"""
""" 
def calculate(**kwargs):
    for key, value in kwargs.items():
        print(f"key={key}, value={value}")

calculate(num_1=3, num_2=5, operator="+")
"""
""" 
age_of_people = {
        "John" :0,
        "Edriane" :0,
        "Lish":0,
        "Doe":0,
    }

reverse_dict = {
    "a" : 0,
    "b" : 0,
    "c" : 0,
    "d" : 0
}

dict_list = {
    "a" : 0,
    "b" : 0,
    "c" : 0,
    "d" : 0
}



def max_age_of_people ():

    highest_age = max(age_of_people.values())

    for name, age in age_of_people.items():

        if age == highest_age:
            print (f"The highest age is: {name} with the age of {age}")

    return " "

def reverse():


    for letter in reverse_dict:
        print (f"{reverse_dict [letter]} : {letter}" )
        
    return " "

def dictionary_list ():

    convert = list(dict_list.items())

    return convert

print ("1. First problem")
print ("2. Second problem")
print ("3. Third problem")

choice = input ("Enter your choice in the problem: ")

match choice:

    case "1":
        os.system('cls')
        age_of_people["John"] = int(input("Enter the age for John: "))
        age_of_people["Lish"] = int (input("Enter the age for lish: "))
        age_of_people["Doe"] = int (input("Enter the age for Doe: "))
        age_of_people["Edriane"] = int (input("Enter the age for Edriane: "))

        print (max_age_of_people())
    
    case "2":
        os.system('cls')
        reverse_dict["a"] = int (input("Enter the first value: "))
        reverse_dict["b"] = int (input("Enter the second value: "))
        reverse_dict["c"] = int(input("Enter the third value: "))
        reverse_dict["d"] = int(input("Enter the fourth value: "))

        print (reverse())
    case "3":
        os.system('cls')
        dict_list["a"] = int(input("Enter the value for a: "))
        dict_list["b"] = int(input("Enter the value for b: "))
        dict_list["c"] = int(input("Enter the value for c: "))
        dict_list["d"] = int(input("Enter the value for d: "))

        print (dictionary_list())
    case _:
        print ("Choice is invalid")
"""

""" 
sum_of_dict = {
    "sum": []
}

min_of_dict = {
    "min_num": []
}

even_of_dict = {
    "only_even": []
}

odd_of_dict = {
    "only_odd": []
}

occure_of_dict ={
    "find_num": []
}
def sum_of_num_list (range_of_list):

    for num in range (0, range_of_list):
        ele_of_list = int (input("Enter the element inside the key: "))
        sum_of_dict["sum"].append(ele_of_list)

    for num in sum_of_dict.items():
        total_sum = sum(sum_of_dict["sum"])

    print (f"The total sum of the list inside the dictionary: {total_sum}")

    return " "

def min_of_num_list (range_of_list):

    for num in range (0, range_of_list):
        ele_of_list = int(input("Enter the element inside the key: "))
        min_of_dict["min_num"].append(ele_of_list)

    min_number_inside = min(min_of_dict["min_num"])


    print (f"The minimum number inside the key is: {min_number_inside}")
    
    return " "

def eve_of_list (range_of_list):

    for num in range (0, range_of_list):
        ele_of_list = int(input("Enter the element inside the list: "))
        even_of_dict["only_even"].append(ele_of_list)


    for num in even_of_dict["only_even"]:
        if num %2 == 0:
            print (f"the even number inside the list of {even_of_dict['only_even']}: {num}") 

    return " "

def odd_of_list (range_of_list):

    for num in range (0, range_of_list):
        ele_of_list = int(input("Enter the element in the keys: "))
        odd_of_dict["only_odd"].append(ele_of_list)

    for num in odd_of_dict["only_odd"]:
        if num %2 == 1:
            print (f"The odd number inside the list of {odd_of_dict['only_odd']}: {num}")
    
    return " "

def occur_of_list (range_of_list):
    count_occur = 0
    look_num = int(input("Enter the number you are looking: "))

    for num in range (0, range_of_list):
        ele_of_list = int(input("Enter the element of the keys: "))
        occure_of_dict["find_num"].append(ele_of_list)

    for num in occure_of_dict["find_num"]:
        
        if num == look_num:
            count_occur = count_occur + 1

    print (f"The occurance of the number: {count_occur}")

    return " "

while True:
    os.system('cls')
    print ("1. Sum of list in dictionary")
    print ("2. Min number of list in dicitionary")
    print ("3. Even number of list in dicitionary")
    print ("4. Odd number of list in dictionary")
    print ("5. Occurance of the number of list in dictionary")
    print ("6. Exit")

    choice = input("Enter the choice of problem: ")

    if choice == "Exit" or choice == "exit":
        break

    match choice:
        case "1":
            os.system('cls')
            range_of_list = int(input("Enter the range of the list: "))
            print(sum_of_num_list(range_of_list))
            input("Press enter to continue")

        case "2":
            os.system('cls')
            range_of_list = int(input("Enter the range of the list: "))
            print(min_of_num_list(range_of_list))
            input("Press enter to continue")
        case "3":
            os.system('cls')
            range_of_list = int(input("Enter the range of the list: "))
            print (eve_of_list(range_of_list))
            input("Press enter to continue")

        case "4":
            os.system('cls')
            range_of_list = int(input("Enter the range of the list: "))
            print (odd_of_list(range_of_list))
            input("Press enter to continue")
        case "5":
            os.system('cls')
            range_of_list = int(input("Enter the range of the list: "))
            print (occur_of_list(range_of_list))
            input("Press enter to continue")
        case _:
            print ("Invalid choice")
"""

""" 
sum_dict = {
    "number_1": 0,
    "number_2": 0,
    "number_3": 0,
    "number_4": 0,
    "number_5": 0,

}

even_dict = {
    "number_1": 0,
    "number_2": 0,
    "number_3": 0,
    "number_4": 0,
    "number_5": 0,

}

factor_dict = {
    "number_1": 0,
    "number_2": 0,
    "number_3": 0,
    "number_4": 0,
    "number_5": 0,

}

def sum_key ():
    total_sum = 0

    if 0 in sum_dict.values():
            print ("Theres a key value 0")
            return " " 
    else:
        total_sum = sum(sum_dict.values())
        print (f"The total sum of key: {total_sum}")

    return " "

def even_key ():
     
    
    even_numbers = {num: value for num, value in even_dict.items() if value %2 == 0}
    
    print (f"The even numbers inside the dictionary: {even_numbers}")

    return " "

def factor_key ():
    total_factor = 1

    for key, num in factor_dict.items():
        total_factor = num * total_factor
    
    print (f"The total factor of the number is: {total_factor}")

    return " "
os.system('cls')
print ("1.Sum of key")
print ("2. Even or odd in key")
print ("3. Factorial of key")

choice = input("Enter your choice of problem: ")

match choice:
    case "1":
        os.system('cls')
        sum_dict["number_1"] = int(input("Enter a number: "))
        sum_dict["number_2"] = int(input("Enter a number: "))
        sum_dict["number_3"] = int(input("Enter a number: "))
        sum_dict["number_4"] = int (input("Enter a number: "))
        sum_dict["number_5"] = int (input("Enter a number: "))

        print (sum_key())

    case "2":
        os.system('cls')
        even_dict["number_1"] = int(input("Enter a number: "))
        even_dict["number_2"] = int(input("Enter a number: "))
        even_dict["number_3"] = int(input("Enter a number: "))
        even_dict["number_4"] = int (input("Enter a number: "))
        even_dict["number_5"] = int (input("Enter a number: "))
     
        print (even_key())

    case "3": 
        os.system('cls')
        factor_dict["number_1"] = int(input("Enter a number: "))
        factor_dict["number_2"] = int(input("Enter a number: "))
        factor_dict["number_3"] = int(input("Enter a number: "))
        factor_dict["number_4"] = int (input("Enter a number: "))
        factor_dict["number_5"] = int (input("Enter a number: "))
        print (factor_key())
    case _:
        print ("Choice invalid")
"""
""" 
name_dict = {

}

for num in range (5):
    name = input (f"Enter your name {num + 1}: ")
    name_dict[f"name_{num + 1 }"] = name


print (name_dict)

"""
""" 
odd_dict = {
    "number":0, 
}

even_dict = {
    "number": 0,
}

occur_dict = {
    "number": 0,
}

rename_dict = {

    "example_1": 0,
    "example_2": 0,
}


def odd_function (range_count):
    sum_of_dict = 0
    for num in range (range_count):
        odd_dict[f"number {num + 1}"] = int(input("Enter the number in key: "))


    sum_dict =  sum(value for value in odd_dict.values() if value %2 == 1 )

    print (f"The sum of the odd number: {sum_dict}")
    return " "

def even_function (range_count):
    sum_of_even_dict = 0
    for num in range (range_count):
        even_dict[f"number {num + 1}"] = int(input("Enter the number in key: " ))

    sum_even_dict = sum(value for value in even_dict.values() if value %2 == 0)
    print (f"The sum of even numbers: {sum_even_dict}")

    return " "

def occur_function (range_count):
    total_occur = 0
    for num in range (range_count):
        odd_dict[f"number {num + 1}"] = int (input("Enter the element in key: "))
    num_search = int(input("Enter the number you want to find in the dictionary: "))

    for key, value in odd_dict.items():

        if value == num_search:
            total_occur = total_occur + 1

    print (f"The total occurance of the number is: {total_occur}")

    return " "

def rename ():
    print ("Follow the format name you want to rename")
    input_name = input("Enter the new name for the key (example_1 or example_2:) ")
    
    if input_name in rename_dict:
        new_name = input(f"Enter the new value for {input_name}: ")
        rename_dict[new_name] = rename_dict.pop(input_name)
    
    print (rename_dict)

    return " " 

def list_to_dict ():
    key_list = ["Edriane", "Alicia", "Whitey", "Nigs"]
    value_list = ["1", "2", "3", "4"]
    res_dict = dict()
    for num in range (len(key_list)):
        res_dict.update({key_list[num]: value_list[num]})

    print (res_dict)

    return " "

while True:
    os.system('cls')
    print ("1. Sum of odd in dictionary")
    print ("2. Sum of even in dictionary")
    print ("3. Occurance of number in dictionary")
    print ("4. Rename key of dictionary")
    print ("5. Convert a list into a dictionary")
    print ("Exit")
    choice = input("Enter your choice: ")

    if choice == "exit" or choice == "Exit":
        break
    match choice:
        case "1":
            os.system('cls')
            range_of_function = int (input("Enter the range of the function: "))
            odd_function(range_of_function)
            input("Press enter to continue")
        case "2":
            os.system ('cls')
            range_of_function = int(input("Enter the range of function: "))
            even_function(range_of_function)
            input("Press enter to continue")
        case "3":
            os.system('cls')
            range_of_function = int(input("Enter the range of function: "))
            occur_function(range_of_function)
            input("Press enter to continue")
        case "4":
            os.system('cls')
            print (rename())
            input("Press enter to continue")
        case "5":
            os.system('cls')
            print (list_to_dict())
            input("Press enter to continue")
        case _:
            print ("Invalid choice")
"""

""" 
my_sibling_dict = {
    "Brother" : {
        "name" : "Eduard",
        "age"  : 28,
        "job"   : "Graphics motion designer"
    
    },

    "Sister" : {
        "name" : "Leiyan",
        "age"  : 23,
        "job"  : "Sk kagawad"
    }

}

my_parent_dict = {
    "Mother": { 
        "name" : "Lielani",
        "age" : 42,
        "job" : "Caddy"
    },

    "Father":{
        "name" : "Eduardo",
        "age" : 42,
        "job" : "Caddy"
    }

}

even_dict = {
    "number": 0,
        
}
def merge_dict ():

    my_family_dict = {
        **my_sibling_dict, **my_parent_dict
    }

    print (my_family_dict)

    return " "

def search_in_dict (search_value):
    
    if search_value in my_sibling_dict:
     print ("Follow the format, (name, age, job)")
     find_key = input(f"Enter you want to know in my: ")
     
     value = my_sibling_dict[search_value][find_key]
     print (f"Data you search is: {value}")
    
    return " "

def min_age_dict_siblings ():
    min_value = min(
        sub_dict["age"]
        for sub_dict in my_sibling_dict.values()

    )

    print (f"The minimun age of my sibling is: {min_value}")
    return " "

def rename_key_parent (value_key):
    
    if value_key in my_parent_dict:
        new_name = input(f"Enter the new value for {value_key}: ")
        my_parent_dict[new_name] = my_parent_dict.pop(value_key)

    print (my_parent_dict)

    return " "

def even_key (range_of_key):

    for num in range (range_of_key):
        even_dict[f"number {num + 1}"] = int (input("Enter the number inside the key: "))

    for value in even_dict.values():
        if value == 0:
            print(" ")
        elif value %2 == 0:
            print (f"{value} is a even number")
        
    return " "

while True:
    os.system('cls')
    print ("1. Merge to dictionaries into one")
    print ("2. Check the value if it's exist in dictionary")
    print ("3. Get the key min value")
    print ("4. Change the value of key in a nested dictionary")
    print ("5. Get the even value in key")
    print ("Exit")

    choice = input("Enter your choice of prob: ")

    if choice == "Exit" or choice == "exit":
        break

    match choice:
        case "1":
            os.system('cls')
            print (merge_dict())
            input("Press enter to continue")
        case "2":
            os.system('cls')
            print ("Follow the format, (Brother, Sister)")
            search_input = str(input("Enter the which value you want to search in my siblings: "))
            search_in_dict(search_input)
            input("Press enter to continue")
        case "3":
            os.system('cls')
            print (min_age_dict_siblings())
            input("Press enter to continue")
        case "4":
            os.system('cls')
            print ("Follow the format, (Mother, Father)")
            key_info = input("Enter the new name for (Mother, Father): ")
            print (rename_key_parent(key_info))
            input("Press enter to continue")
        case "5":
            os.system('cls')
            range_of_key = int (input("Enter the range of the number: "))
            print (even_key(range_of_key))
            input("Press enter to continue")
        case _:
            print ("Invalid choice")
"""
""" 
my_nums = {
    "number": 0,
    
}

def odd_sum ():
    total_sum = 0
    counter = 1
    while True:
        value = int(input("Enter the number 0 to stop: "))
        if value == 0:
            break

        my_nums[f"number {counter}"] = value
        counter = counter + 1

    total_sum = sum(my_nums.values())

    print (f"The total sum: {total_sum}")

    return " "


odd_sum()
"""
""" 
def calculate_average (numbers):
    total = sum (numbers)
    average = total / len (numbers)

    return average


numbers = []
user_input = input("Enter a number: ")

while user_input.isnumeric():
    numbers.append(int(user_input))
    user_input = input("Enter a number: ")

print ("Average: ", calculate_average(numbers))
"""
dict_word ={}
def occur_of_letter (input_word):
    for num in input_word:
        if num in dict_word:
            dict_word[num] += 1
        else:
            dict_word [num] = 1

    print (dict_word)

    return " "

def letter_finder (input_word):
    occurance_of_letter = 0
    search_letter = str(input("Enter a word you want to find: "))

    for num in input_word:
        if search_letter == num:
            occurance_of_letter += 1 

        else:
            occurance_of_letter = 1
    
    print (f"The occurance of the letter {search_letter} is: {occurance_of_letter}")

    return " "

ave_dict = {
    "nums": 0,
}

def dict_ave (range_of_dict):
    total_sum = 0
    for num in range (1, range_of_dict + 1):
        number = int(input("Enter a number inside the dictionary: "))
        ave_dict[f"nums{num}"] = number
        
   
    for num in ave_dict.values():
        total_sum = num + total_sum

    length_of_dict = len(ave_dict)

    total_ave = total_sum / length_of_dict
    
    print (f"The total average of the list: {total_ave: }")




print ("1. Occurance of the letter in a word")
print ("2. Occurance of the inputted letter in a word")
print ("3 . Average of a dict")
choice = input("Enter your choice of problem: ")

match choice:
    case "1":
        os.system("cls")
        word_input = str(input("Enter a word: "))
        occur_of_letter(word_input)
    case "2":
        os.system('cls')
        word_input = str(input("Enter a word: "))
        letter_finder(word_input)
    case "3":
        os.system('cls')
        range_of_loop = int (input("Enter the range of the loop: "))
        dict_ave(range_of_loop)
    case _:
        print ("Invalid of choice")


def format_name(f_name, l_name):
  """Take a first and last name and format it to title case."""
  if f_name == "" or l_name == "":
      return "You didn't provide valid inputs."
  formatted_f_name = f_name.title()
  formatted_l_name = l_name.title()
  return f"{formatted_f_name} {formatted_l_name}"
