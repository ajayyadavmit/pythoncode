# MAKE FLEXIBLE FUNCTIONS 
# * ARGS ARGUMENTS IN THE FUNCTIONS.. 
#  STAR * OPERATOR IN THE FUNCTION 

# argument combined will be creaed to TUPLE () print type of args 


def total(*args):
    t = 0
    print(type(args))
    print(args)
    for num in args:
        t = t + num
    return t

print(total(5,4,6))

s = [4,3,8]
m = (4,3,2)
print(total(*m))  # By the STAR argument , it will UNPACK the argument of LIST / TUPLES. 

# paramerter vs arguments in funtion 
# on the function definition >> variables ae called as PARAMETERS 
# ON function defining >> variables are called as arguments.. 


## DOUBLE START OPERATOR  **KWARGS    **KWARGS  KWARGS >> KEY WORD ARGUMENTS 
# KWARGS FOR THE dictionary TYPE values.. {}  
# ARGS FOR THE tuple data types.  ()  brackets () parenthesis bracket () >> 

# UnPacking the Arguments in the tuple () with Star Operator *args 
# UnPacking arguments in the Dictionary Object {} with the Double Star Operator **kwargs 


def personDetails(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for k,v in kwargs.items(): 
        print(f" the name is {k} and the place is {v}")
    
d = dict(a = "df", b = "dfdfdfdfd")

personDetails(name = "ram", place = "ktm", **d)

print(d)
print(type(d))

# keyword arguments means to have argument like in key== vailue pairs .. kV is the dictionary items

d2 = {"subject": [45,34,78]}

def five(**kwargs):
    print(type(kwargs))
    for k,v in kwargs.items():
        print(k,v)
        print(kwargs[k])
l1 = [4,34,89,67]
five(subject = [4,34,89,67], name = "english")

