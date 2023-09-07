import random
import hangman_art
import hangman_words

print(hangman_art.logo)

lives = 6

word = random.choice(hangman_words.word_list)
display = len(word) * ["_"]

print(f'Pssst, the solution is {word}.')

while '_' in display:
    letter = input("Guess a letter: ").lower()
    if letter in display:
        print(f"You've already guessed {letter.upper()} letter.")

    gussed = False
    for i, l in enumerate(word):
        if l == letter:
            gussed = True
            display[i] = letter
    if gussed is False:
        lives -= 1
        print(hangman_art.stages[lives])
        print(f"Letter {letter.upper()} is not in the word")

    print(f"{' '.join(display)}")

