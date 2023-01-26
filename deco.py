# DECORATORS ENHANCE the existing fuctionality of the function. ().. 
# decorators are used iwht the @  at the rate @ sysmbol above the function. 
# it pass the function as the arguments. .. Function inside function .. 
# decorator is the function only that ehance current function funcatlity .. 
# as an input as a function.. since it ehance function functionality existings types... 
# deocrators used as a syntactic sugar  for increase of function functionality property behaviour. 
# This can be written in the short hand using the SYNTACTIC SUGAR Types with the DECORator function. 
# Decorator is the SYNTACTIC SUGAR type where it enhances the function functionality types. 
# # Outer and Inner Functions.
# # RETURNIGN OF FUNCTION CALL WITH ()  OR WITHOUT () BRACKETS PARENTHESIS... 

# def outer_func():
#     def inner_func():
#         print("Inside the Inner function")
#     return inner_func

# var = outer_func()
# var()

# def outer_functwo(msg):
#     def two():
#         print(f" Greetings >> {msg}")
#     return two

# of = outer_functwo("HI GOOD MORNING")
# print(type(of))
# of()

# # FUNCTION AS AN ARGUMENT PASSING >> MAP ()  >> FILTER >> REDUCE () 

# passing function as an argument 
x = 5 
print((lambda x : x * 8) (x))

l = [5,43,898,45,322,450]
print([  {i: i + 22} for i in l   ])

print(list(map(lambda x: x + 2, l)))


def square(x):
    return x*x

def cube(x):
    return x*x*x 

print(list(map(square, l)))

def calculate(func1, l):
    a =[]
    for i in l: 
        a.append(func1(i))
    return a 

print(calculate(cube,l))

# return function as an argument return types 
# return function as arguments means value of Written Type is Function Value. .. 
# << FUNCTION INSIDE ANOTHER FUNCTION TYPES... >> 

def nepali():
    def loc(a):
        print(f"place is at {a}")
    print("Nepali") ; return loc    

n1 = nepali()
print(type(n1))

n1("Janakpur")

print("#"* 33)

def decoratorfunc(func1):
    def wrapperfunc():
        print("inside the wrapper function")
        func1()
    return wrapperfunc

@decoratorfunc
def one():
    print("Inside ONE ONE ")

def two():
    print("inside TWO TWO >>")

# o1 = decoratorfunc(one)
# o1()


print(type(one))

one()


def twoDecorator(f1):
    def wrapper():
        print(" this is inside WRAPPER FUNC")
        f1()
    return wrapper

@twoDecorator
def kind():
    print("kind value KIND")
    return "kind"


kind()






