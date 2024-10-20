import os

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
    
os.system ('cls')
print ("1. A function that returns the sum of the list")
print ("2. A function that returns the average of the items")
print ("3. A function that returns the highest value in the list")
print ("4. A function that returns the factorial of the number")
print ("5. A function that Identify the number if it's prime or not and returns the value")

choice = input("Enter the choice of the problem: ")

match choice:
    case "1":
        os.system('cls')
        range_list_1 = int(input("Enter the range of the list: "))
        print (f"The sum of the list: {sum_of_list (range_list_1)}")

    case "2":
        os.system ('cls')
        range_list_2 = int(input("Enter the range of the list: "))
        print (f"The total average of the array: {average_of_list(range_list_2)}")
    
    case "3":
        os.system ('cls')
        range_list_3 = int(input("Enter the range of the list: "))
        print (f"The highest number in the array: {highest_value(range_list_3)}")

    case "4":
        os.system('cls')
        num = int(input("Enter the range of the element: "))
        print (f"The factorial number of the list: {factorial_num(num)}")

#NO PROBLEM NUMBER 5