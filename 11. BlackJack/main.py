import random
import art

ACE = 11
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user = { "cards": [], "score": 0 }
computer = { "cards": [], "score": 0 }

def deal_card():
    return random.choice(cards)

def calculate_score(oponent):
    oponent["score"] = sum(oponent["cards"])
    if oponent["score"] > 21:
        if ACE in oponent["cards"]:
            oponent["cards"].remove(ACE)
            oponent["cards"].append(1)
            calculate_score(oponent)

def compare_opponents():
    if computer["score"] == 21:
        return f"You LOOSE.\nComputer has BlackJack!\nYour score is {user['score']}"
    elif user["score"] == 21:
        return "You WIN.\nYou have BlackJack!\nComputer score is {computer['score']}"
    elif user["score"] == computer["score"]:
        return f"It's a TIE.\nYour score is {user['score']} and Computer score is {computer['score']}"
    elif user["score"] > computer["score"]:
        return f"You WIN.\nYour score is {user['score']} and Computer score is {computer['score']}"
    elif user["score"] < computer["score"]:
        return f"You LOOSE.\nYour score is {user['score']} and Computer score is {computer['score']}"

if __name__ == '__main__':
    print(art.logo)
    user["cards"].append(deal_card())
    next_card = 'yes'
    game_end = False
    while next_card == 'yes':
        user["cards"].append(deal_card())
        calculate_score(user)
        if user["score"] > 21:
            game_end = True
            print(f"\nYou LOSE.\nYour score is {user['score']} and Computer score is {computer['score']}")
            break
        print(f'You have cards {user["cards"]} and your score is {user["score"]}')
        next_card = input("Would you like to get another card? ('yes' or 'no') ")

    if not game_end:
        computer["cards"].append(deal_card())
        computer["cards"].append(deal_card())
        calculate_score(computer)
        while computer["score"] < 17:
            computer["cards"].append(deal_card())
            calculate_score(computer)
        if computer["score"] > 21:
            game_end = True
            print(f"\nYou WIN.\nYour score is {user['score']} and Computer score is {computer['score']}")

    if not game_end:
        print("\n" + compare_opponents())
