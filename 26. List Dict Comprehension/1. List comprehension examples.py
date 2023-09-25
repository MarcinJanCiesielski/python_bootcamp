numbers = [1, 2, 3]
new_numbers = [n +1 for n in numbers]

print(new_numbers)


name = "Marcin"
chars = [letter for letter in name]
print(chars)

range_list = [num * 2 for num in range(1, 5)]
print(range_list)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleonor', 'Freddie']
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names_upper = [name.upper() for name in names if len(name) > 4]
print(long_names_upper)
