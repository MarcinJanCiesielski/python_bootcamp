with open("my_file.txt", encoding="utf8") as file:
    content = file.read()
    print(content)

with open("my_file.txt", encoding="utf8", mode="a") as file:
    content = file.write("\nNew text")
    print(content)
