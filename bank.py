import random
cards = []
taken_numbers = {"-1": True}
logged_in = False
quit = False

class Card:
    def __init__(self, number, pin):
        self.number = number
        self.pin = pin
        self.balance = 0

def generate_card():
    card_num = "-1"
    while taken_numbers.get(card_num) is not None:  
        card_num = "400000" + str(random.randint(1000000000, 9999999999))
    card_pin = str(random.randint(0000, 9999))
    taken_numbers[card_num] = True
    cards.append(Card(card_num, card_pin))
    print("\nYour card has been created.")
    print("Your card's number:")
    print(card_num)
    print("Your card's pin:")
    print(card_pin)
    return 0

def validate_card(number, pin):
    for card in cards:
        if card.number == number and card.pin == pin:
            return card
    return False


while not quit:
    #Sequence for user that is not logged into a card
    if not logged_in:
        print("\n1. Create an account")
        print("2. Log into account")
        print("0. Exit")
        choice = -1
        while choice < 0 or choice > 2:
            choice = int(input())
        if choice == 1:
            generate_card()
        elif choice == 2:
            user_card_number = input("\nEnter your card's number: \n")
            user_card_pin = input("Enter your card's pin: \n")
            current_card = validate_card(user_card_number, user_card_pin)
            if not current_card:
                print("Error: Wrong card number or PIN.")
            else:
                logged_in = True
                print("You have successfully logged in.")
        else:
            print("Bye!")
            quit = True
    #Sequence for user that is logged in 
    else:
        print("\n1. Balance")
        print("2. Logout")
        print("0. Exit")
        choice = -1
        while choice < 0 or choice > 2:
            choice = int(input())
        if choice == 1:
            print("Balance: {}".format(current_card.balance))
        elif choice == 2:
            print("You have successfully logged out.")
            logged_in = False
        else:
            print("Bye!")
            quit = True


