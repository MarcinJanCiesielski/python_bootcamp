from morse_alphabet import ALPHABET_TO_MORSE

def encrypt(text: str) -> str:
    morse_code = ''

    for ch in text_to_morse.upper():
        try:
            morse_code += f'{ALPHABET_TO_MORSE[ch]} '
        except KeyError:
            continue
    
    return morse_code


text_to_morse = input("Provide text to convert into Morse' Code: ")

print(f"Your Morse Code is:\n{encrypt(text_to_morse)} ")
