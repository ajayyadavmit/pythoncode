# Eval() funtion is the built-in function in Python . 
# eval() function PARSES the string ARGUMENT AND TREATS IT AS AN PYTHON ..  EXPRESSION. pr

print(dir(__builtins__))

for i in dir(__builtins__): 
    if "eval" in i: 
        print("present")

# eval() function will make String argument as a Python Expression.  Expression is operaor and operand features.. 
# evaluate expresson >> eval( expression, local = None, global = None) >> global , locals are DIctionary 


# ch = eval(input("Enter the choice"))

# ch = (input("Enter the choice"))
ch = 0
match ch:
    case 'ab': pass
    case 'cd' : print("CDCD CD  CD ")
    case 5 : print("FIVE")
    case [3,4,5] : print("LISTING VALUES")
    # case {2,3} : print("SET Values ")
    case {"name" : 54, "loc" : "ktm"} : print("dictionary value")
    case default:  print("Defualt values ")

num = 3 

a= "num ** num"
print(type(eval(a)))

l1 = [2,3,4]
l2 = [4,5,6]

print(eval('[3,4]+[5,89,7]'))

# print(eval("dfdf"+ "sdfsfs"))

# x = int(input("Enter the Expression "))

# y = "x * (x + 3) * (x + 1)"

# print(eval(y))

# Evals function is mostly used in the following scenarios.. 
# for the Mathematical functions expressions as String
# to take INPUTS as Tuple, List, Dictioary in EVAL 

p = eval(input("Enter P value"))
r = eval(input("Enter RR value"))

print(p+r)



