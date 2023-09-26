def add(*args):
    total = 0
    for n in args:
        total += n
    
    return total

print(add(1,2,3,4,5,6))


def calculate(n, **kwarg):
    print(kwarg)
    for key, value in kwarg.items():
        print(key, value)
    n += kwarg["add"]
    n *= kwarg["multiply"]
    print(n)

calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs) -> None:
        self.make = kwargs.get("make") # jeżeli nie ma wartości w słowniku to nie spowoduje błędu i zostanie zwrócony None
        self.model = kwargs.get("model") # jeżeli nie ma wartości w słowniku to nie spowoduje błędu i zostanie zwrócony None



my_car = Car(make="Nissan", model="GT-R")
arr = [1, 2,3,4,5,6]
print(arr)
print(*arr)
