# #FileNotFound
# try:
#     file = open('a_file.txt', encoding="utf8")

#     a_dict = {"key":"value"}
#     value = a_dict["non_existing_key"]

# except FileNotFoundError:
#     file = open('a_file.txt', encoding="utf8", mode="w")
#     file.write("Something")

# except KeyError as error_message:
#     print(f"That key {error_message} does not exist")

# else: #wykonywany, jeżeli wszystko poszło OK 
#     content = file.read()
#     print(content)

# finally:
#     file.close()
#     print("File was closed")

#     raise KeyError("Thie is an error I've made up")

#KeyError


#IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

#Type Error
# text = "abc"
# print(text + 5)


height = float(input("Height [m]: "))
weight = int(input("Weight [kg]: "))

if height > 3:
    raise ValueError("Human height should not be over 3m.")

bmi = weight / height ** 2
print(bmi)
