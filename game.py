import random
import os 




def slot_game(input_balance):
    slot_list = ["Apple", "Grapes", "Orange"]

    if input_balance != 0:
        print (f"Your total balance is: {input_balance}: ")
        input_continue = str(input("Do you want to to play Y/N? "))
        input_continue.upper()

        if input_continue == "Y" or input_continue == "y":
            random_result = random.choices(slot_list, k = 3)
            print (f"The result of slot is: {random_result}")

            if random_result[0] == random_result [1] and random_result [0] == [2]:
                input_balance = input_balance + 5
                print (f"Your total balance is: {input_balance}")
            elif random_result [1] == random_result [0] and random_result [1] == random_result [2]:
                input_balance = input_balance + 5
                print (f"Your total balance is: {input_balance}")
            elif random_result [2] == random_result [0] and random_result [2] == random_result [1]:
                input_balance = input_balance + 5
                print (f"Your total balance is: {input_balance}")
            elif random_result[0] == random_result[1] or random_result[0] != random_result[2]:
                input_balance = input_balance + 1
                print (f"Your total balance is: {input_balance}")
            elif random_result[0] == random_result [2] or random_result [0] != random_result[1]:
                input_balance = input_balance + 1
                print (f"Your total balance is: {input_balance}")
            elif random_result[1] == random_result [0] or random_result[1] != random_result[2]:
                input_balance = input_balance + 1
                print (f"Your total balance is: {input_balance}")
            elif random_result[1] == random_result[2] or random_result[1] != random_result[0]:
                input_balance = input_balance + 1
                print(f"Your total balance is: {input_balance}")
            elif random_result[2] == random_result[0] or random_result[2] != random_result[1]:
                input_balance = input_balance + 1
                print (f"Your total balance is: {input_balance}")
            elif random_result[2] == random_result[1] or random_result[2] != random_result[0]:
                input_balance = input_balance + 1
                print (f"Your total balance is: {input_balance}")
            elif random_result[0] != random_result[1] and random_result[0] != random_result[2]:
                input_balance = input_balance - 5
                print (f"Your total balance is: {input_balance}")
            elif random_result[1] != random_result[0] and random_result[1] != random_result[2]:
                input_balance = input_balance - 5
                print (f"Your total balance is: {input_balance}")
            elif random_result[2] != random_result[1] and random_result[2] != random_result[0]:
                input_balance = input_balance - 5
                print (f"Your total balance is: {input_balance}")
                
        else:
            print ("Thank you for playing the game ")
            pass

    else:
        print (f"Not enough balance: {input_balance}")

def baccarat_card_game (input_balance):

    if input_balance > 0:
        choice_input = input("Press Y to continue N to stop: ")
        
        if choice_input == "Y":
            place_bet = (input("Enter your bets on (Banker/Player): "))
            random_card_one = random.randint(1, 9)
            random_card_two = random.randint (1, 9)
            random_card_three = random.randint(1, 9)
            random_card_four = random.randint(1, 9)

            result_banker = (random_card_one + random_card_two) % 10
            result_player = (random_card_three + random_card_four) % 10
            os.system ('cls')
            print ("Banker")
            print (f"The value of the first card {random_card_one} and the value of the second card {random_card_two}")
            print (f"The result of banker: {result_banker}")
            input("Press enter to see the next card")
            print ("Player")
            print (f"The value of the first card {random_card_three} and the value of the second card {random_card_four}")
            print (f"The result of the player: {result_player}")

            
            if place_bet == "Banker":
                if result_banker > result_player:
                    input_balance = input_balance + input_balance
                    print (f"Banker wins: {result_banker}")
                    print (f"Your total credit is: {input_balance}")
                elif result_banker < result_player:
                    input_balance = input_balance - input_balance
                    print (f"Player wins: {result_player}")
                    print (f"Your total balance is: {input_balance}")
                else:
                    print ("It's a draw")

            elif place_bet == "Player":
                if result_player > result_banker:
                    input_balance = input_balance + input_balance
                    print (f"Player wins: {result_player}")
                    print (f"Your total credit is: {input_balance}")
                elif result_player < result_banker:
                    input_balance = input_balance - input_balance
                    print (f"Banker wins: {result_banker}")
                    print (f"Your total balance is: {input_balance}")
                else:
                    print ("It's a draw")

        else:
            pass

    else:
        print ("Not enough balance")


def guest_the_num ():
    input_balance = int(input("Top up a credit: "))

    random_number = random.randint(1, 9)

    if input_balance > 0:
        input_guest = int(input("Enter a guessing number: "))
        print (f"Your guess number is: {input_guest}")
        input("Press enter to see the if your guest is correct")
        print (f"The random number is: {random_number}")

        if input_guest == random_number:
            input_balance = input_balance + input_balance
            print (f"Your guest is the right number: {random_number}")
            print (f"Your current balance is: {input_balance}")
        elif input_guest != random_number:
            input_balance = input_balance - input_balance
            print (f"Your guest is the wrong number: {random_number}")
            print (f"Your current balance is: {input_balance}")
        else:
            input_balance = input_balance = input_balance
            print (f"Your guest number is: {input_guest}")
            print (f"The random number is: {random_number}")
            print ("It's a draw")
    else:
        print ("You have no enough credits")
        pass

while True:
    os.system('cls')
    print ("1. Slot game")
    print ("2. Baccarat game")
    print ("3. Guess the number")
    print ("Exit")

    choice = str(input("Enter your choice of game: "))

    if choice == "Exit" or choice == "exit":
        break

    match choice:
        case "1":
            os.system('cls')
            print ("Slot game")
            balanace_player = int(input("Top up a credit: "))
            slot_game(balanace_player)
            input("Press enter to continue")
        case "2":
            os.system("cls")
            print ("Baccarat game")
            balanace_player = int(input("Top up a credit: "))
            baccarat_card_game(balanace_player)
            input("Press enter to continue")
        case "3":
            os.system('cls')
            print ("Guess the number from 1 - 9")
            guest_the_num()
            input("Press enter to continue")
        case _:
            print ("Invalid choice")