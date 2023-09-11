import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shifted_alphabet, direction):
    result = ''
    for letter in text:
        if letter in alphabet:
            if direction == 'encode':
                result += shifted_alphabet[alphabet.index(letter)]
            elif direction == 'decode':
                result += alphabet[shifted_alphabet.index(letter)]
        else:
            result += letter

    print(f"The text is: {result}")


def main():
    print(art.logo)

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > len(alphabet):
        shift = shift % len(alphabet)

    shifted_alphabet = alphabet[shift : ] + alphabet[ : shift]

    caesar(text, shifted_alphabet, direction)

    again = input("Do you want to use Caesar Cipher again (yes / no)? ")
    if again == 'yes':
        main()

if __name__ == "__main__":
    main()
