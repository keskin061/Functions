# A simple function
def greet_user():
    print("Hello")


greet_user()


# passing an argument
def greet_user_arg(name):
    print(f"Hello {name}")


greet_user_arg("keskin")


# default value for parameters
def make_pizza(toppings="bacon"):
    print(f"have a {toppings} pizza")


make_pizza()
make_pizza("ham")


# returning a value
def add_numbers(a, y):
    return a + y


print(add_numbers(1, 2))
