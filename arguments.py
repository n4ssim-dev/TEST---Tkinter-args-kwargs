# Calculate with *args
from symtable import Class


def add(method="sum",*args):
    if method == "sum":
        args_list = [n for n in args]
        args_sum = 0
        for n in args_list:
            args_sum += n

        return args_sum

    elif method == "divide":
        args_list = [n for n in args]
        args_sum = 1
        for n in args_list:
            divided_number = n / args_sum
            args_sum = n
        return divided_number

    elif method == "multiply":
        args_list = [n for n in args]
        args_n = 1
        for n in args_list:
            multiplied_number = n * args_n
            args_n = n
        return multiplied_number

#print(add("multiply",10,5))

# Calculate with **kwargs

def calculate_2(n,**kwargs):
    n+= kwargs["add"]
    multiplied_number = n * kwargs["multiply"]
    print(multiplied_number)

#calculate_2(2,add=10,multiply=2)

class House:
    def __init__(self,**kwargs):
        self.type = kwargs.get("type")
        self.value = kwargs.get("price")
        self.color = kwargs.get("color")
        self.make_car()

    def make_car(self):
        print(f"You house is a {self.color} {self.type}, it is worth {self.value}$")

house = House(type="villa",price="3 000 000",color="red")