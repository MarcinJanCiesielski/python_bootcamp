import os
import art

print(art.logo)
print("Welcome to the secret auction program")

bidders = {}

def add_bid():
    name = input("What is your name? ")
    bid = input("What's your bid? ")

    bidders[name] = int(bid)

    answer = input("Are there any other bidders? Type 'yes' or 'no' ")
    
    if answer == 'yes':
        os.system('cls' if os.name == 'nt' else 'clear')
        add_bid()

if __name__ == '__main__':
    add_bid()
    highest_bid = 0
    highest_name = ''

    for n, b in bidders.items():
        if b > highest_bid:
            highest_bid = b
            highest_name = n
    
    print(f'{highest_name} has won the auction with bid of {highest_bid}!')

