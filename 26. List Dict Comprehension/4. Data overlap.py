num1 = [int(line.strip()) for line in open('file1.txt').readlines()]
num2 = [int(line.strip()) for line in open('file2.txt').readlines()]

result = [ n1 for n1 in num1 if n1 in num2]

# Write your code above 👆

print(result)
