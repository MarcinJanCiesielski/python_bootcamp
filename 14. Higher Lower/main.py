import random
import os
import art
import game_data

score = 0
game_end = False
questions = game_data.data

def check_answer(ans, vsa, vsb):
    followers = 'follower_count'
    if ans == 'A':
        return int(vsa[followers]) > int(vsb[followers])
    elif ans == 'B':
        return int(vsa[followers]) < int(vsb[followers])
    else:
        return False

print(art.logo)

while not game_end or len(questions) == 0:
    vs_a = random.choice(game_data.data)
    vs_b = random.choice(game_data.data)
    if vs_a['name'] == vs_b['name']:
        break

    print(f"Compare A: {vs_a['name']}, a {vs_a['description']} from {vs_a['country']}")
    print(art.vs)
    print(f"Against B: {vs_b['name']}, a {vs_b['description']} from {vs_b['country']}")
    answer = input("Who has more followers? Type 'A' or 'B': ")

    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(art.logo)
    if check_answer(answer, vs_a, vs_b):
        score += 1
        print(f"You're right! Current score: {score}\n")
    else:
        print(f"Sorry, that's wrong. Final score: {score}\n")
        game_end = True
