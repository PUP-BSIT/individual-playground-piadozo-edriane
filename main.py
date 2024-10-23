import os

"""

Create a file called main.py. The program will ask the user for the following order details:
a. Product Name
b. Price
c. Quantity

After the last detail, it will ask if the user wants to add another item answerable by y for yes or n for no. If the user enters y, it will ask order details. Otherwise, it will proceed to the next step. After the orders are completed, the program will ask for the customer name and senior ID no.(blank if not senior citizen). If the customer is a senior citizen, a 10% discount will be deducted in the grand total. After that, the program will display the the following details:

d. Items(product name, price, quantity, total)
e. Customer Name
f. Senior ID No.
g. Grand Total


"""
list_of_product = ["Nescafe", "Rebisco", "Lucky Me"]




list_of_items_nescafe =  ["Nescafe Creamy white", "Nescafe Original", "Nescafe Classic"]
price_of_items_nescafe = list_of_items_nescafe.copy()
price_of_items_nescafe[0] = 15
price_of_items_nescafe[1] = 15
price_of_items_nescafe[2] = 15



list_of_items_rebisco = ["Rebisco Honey butter", "Rebisco Butter", "Bravo"]
price_of_items_rebisco = list_of_items_rebisco.copy()
price_of_items_rebisco [0] = 7
price_of_items_rebisco [1] = 8
price_of_items_rebisco [2] = 9



list_of_items_lucky_me = ["Chicken Noodles", "Beef Noodles", "Pork Noodles"]
price_of_items_luckyme = list_of_items_lucky_me.copy()
price_of_items_luckyme [0] = 10
price_of_items_luckyme [1] = 12
price_of_items_luckyme [2] = 12

list_of_order = []


def product_name_product_price (prod_wants):

    if prod_wants == 1:
        print(f"The Items in nescafe: {list_of_items_nescafe}")
        print (f"The price of the item in nescafe ₱ {price_of_items_nescafe}")
    elif prod_wants == 2:
        print (f"The items in rebisco: {list_of_items_rebisco}")
        print (f"The price of items in rebisco: ₱ {price_of_items_rebisco}")
    elif prod_wants == 3:
        print (f"The items in Luckyme: {list_of_items_lucky_me}")
        print (f"The price of items in lucky me: ₱ {price_of_items_luckyme} ")
    else:
        print ("Invalid input")

def order_and_quantity (prod_wants, num_of_items):
    total_order = 0
    if prod_wants == 1:
        print ("0 - Nescafe Creamy white. ", "1 -Nescafe Original. ", "2 -Nescafe Classic")
        for num in range (0, num_of_items):
            item_ordered = int (input("Enter the items you want to order: "))
            list_of_order.append (item_ordered)

        for num in list_of_order:
            if 0 <= num or 0 < len(list_of_order):
                value = list_of_items_nescafe[num]
                print (f"The product in the index number: {num} is: {value}")
        
        for num in list_of_order:
            total_price = 0
            total_price = price_of_items_nescafe + total_price

        print (f"The total price: {total_price}")

    elif prod_wants == 2:
        print ("0 - Rebisco Honey butter. ", "1 - Rebisco Butter. ", "2 - Bravo")
        for num in range (0, num_of_items ):
            item_ordered = int (input("Enter the items you want to order: "))
            list_of_order.append (item_ordered)

        for num in list_of_order:
            if 0 <= num or 0 < len(list_of_order):
                value = list_of_items_rebisco[num]
                print (f"The product in the index number: {num} is: {value}")

    elif prod_wants == 3:
        print ("0 - Chicken Noodles. ", "1 - Beef Noodles.", "2 - Pork Noodles.")
        for num in range (0, num_of_items):
            item_ordered = int (input("Enter the items you want to order: "))
            list_of_order.append (item_ordered)

        for num in list_of_order:
            if 0 <= num or 0 <= len(list_of_order):
                value = list_of_items_lucky_me[num]
                print (f"The product in the index: {num} is: {value}")
   
    for num in list_of_order:
        total_order = total_order + num
    
    print (f"The total order is: {total_order}")





os.system ('cls')

print ("a. Product name")
print ("b. Price")
print ("c. Items")


choice = input("Enter your choice: ")

match choice:
    case "a":
        os.system('cls')
        print ("The available product in our store")
        print (list_of_product)
    case "b":
        os.system('cls')
        print ("Price of the product in the store")
        print ("a. For the Nescafe ")
        print ("b. For the Rebisco")
        print ("c. For the Luckyme")

        choice_b = input("Enter your choice: ")

        match choice_b:
            case "a":

                os.system('cls')
                print(f"The Items in nescafe: {list_of_items_nescafe}")
                print (f"The price of the item in nescafe ₱ {price_of_items_nescafe}")
            case "b":

                os.system ('cls')
                print (f"The items in rebisco: {list_of_items_rebisco}")
                print (f"The price of items in rebisco: ₱ {price_of_items_rebisco}")
            case "c":
                
                os.system ('cls')
                print (f"The items in Luckyme: {list_of_items_lucky_me}")
                print (f"The price of items in lucky me: ₱ {price_of_items_luckyme} ")
            case _:
                print ("Invalid choice")


    case "c":
        os.system ('cls')
        print ("a. Product Name and Price")
        print ("b. Quantity")
        print ("c. total")
        choice_c = input("Enter your chosen product: ")

        match choice_c:
            case "a":
                os.system('cls')
                print ("Product Name and Price")
                print ("1. For Nescafe")
                print ("2. For Rebisco")
                print ("3. For Luckyme")
                choice_of_prod = int(input("Enter your chosen product: "))
                product_name_product_price(choice_of_prod)

            case "b":
                os.system('cls')
                print ("Order")
                print ("1. For Nescafe")
                print ("2. For Rebisco")
                print ("3. For Luckyme")
                choice_of_prod = int(input("Enter your chosen producdt: "))
                quantity_of_items = int(input("Enter the quantity of the item: "))
                order_and_quantity(choice_of_prod, quantity_of_items)

            case "c":
                os.system('cls')
                
    case _: 
        print ("Invalid choice")