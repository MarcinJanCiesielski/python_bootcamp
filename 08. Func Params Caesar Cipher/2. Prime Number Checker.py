#Write your code below this line 👇
def prime_checker(number):
    prime = True
    divider = number // 2
    while divider > 1:
        if number % divider == 0:
            prime = False
            break
        divider -= 1
    if prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
