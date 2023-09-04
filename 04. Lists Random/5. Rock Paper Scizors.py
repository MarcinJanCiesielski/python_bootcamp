# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
import random

prs = {"paper": '📜', "rock": '🪨', "scissors": '✂️'}
win_loose = [
    ["rock", "scissors"],
    ["scissors", "paper"],
    ["paper", "rock"]
]


def who_won(computer, human):
    for row in win_loose:
        if computer in row and human in row:
            if row.index(computer) < row.index(human):
                return "Computer won!"
            elif row.index(computer) > row.index(human):
                return "You won!"
            else:
                return "It's a Tie!"


comp = random.randint(0, 2)
human = input("What do you choose (paper / rock / scissors): ").lower()
keys = prs.keys()
if human in keys:
    computer = [*keys][comp]
    print(f"You choose {prs[human]}.")
    print(f"Computer choose {prs[computer]}.")

    print(who_won(computer, human))
