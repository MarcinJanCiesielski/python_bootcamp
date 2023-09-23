#Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

NAMES_FILE = "./Input/Names/invited_names.txt"
LETTER_SCHEME = './Input/Letters/starting_letter.txt'
OUTPUT_PATH = "./Output/ReadyToSend/"
PLACEHOLDER = '[name]'

with open(NAMES_FILE, encoding="utf8") as name_file:
    for name in name_file.readlines():
        name = name.strip("\n")
        with open(LETTER_SCHEME, encoding="utf8") as schema:
            with open(OUTPUT_PATH + f"{name}_letter.txt", mode="w", encoding="utf8") as letter:
                for line in schema.readlines():
                    line = line.replace(PLACEHOLDER, name)
                    letter.write(line)
