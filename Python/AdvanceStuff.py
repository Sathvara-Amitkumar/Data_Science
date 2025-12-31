# Decorator
# def decorate(func):
#     def wrapper(a,b):
#         print("Before the function call.")
#         func(a,b)
#         print("After the function call.")
    
#     return wrapper


# @decorate
# def greeting():
#     print("Hello, World!")

# @decorate
# def addition(a,b):
#     print("The sum is :", a + b)

# addition(5, 10, 11)


# Args and Kwargs Example-------------------------------------

# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum

# print(add(5, 10, 15, 20))


# def info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")

# info(name="John", age=30, city="New York", designation="AI/ML Engineer")

# def decorate(func):
#     def wrapper(*a,**b):
#         print("Before the function call.")
#         func(*a,**b)
#         print("After the function call.")
    
#     return wrapper

# @decorate
# def addition(a,b,c,d):
#     print("The sum is :", a + b + c + d)

# addition(5, 10, 15, 20)


# ------------------------------------------------------------------------

# Comprehensions Example
a = 11
print("Even" if a % 2 == 0 else "Odd")

evod = ["Even" if x % 2 == 0 else "Odd" for x in range(1,6)]
print(evod)

dict_comp = {x : x*x for x in range(1,11)}
print(dict_comp)

set_comp = {x for x in range(1,11)}
print(set_comp)

tuple_comp = tuple(x*x for x in range(1,11))
print(tuple_comp)


# Map and Filter Example
numbers = [1, 2, 3, 4, 5]
square = map(lambda x : x*x, numbers)
print(list(square))

even = filter(lambda x : x % 2 == 0, numbers)
print(list(even))

