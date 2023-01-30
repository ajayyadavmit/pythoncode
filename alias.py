# alias is written for the Function Name 
# Alias can be used with the LAMBDA function 
# LAMBDA is the ANONYMOUS Function i.e. functio without Name 
# ALias can be used with the FUnction INNER function value CALL (). 

# Lambada has 2 parts a. Arugument  ( that pass the value to function )  b. Expression ( python simple expressions values )

alias1 = lambda x,y = 5 : (x + y , x -y)  # Returned as a TUPLE () for the values.. 
print((alias1))   # function object at HEX Values.. 
print(alias1(5,34))
print(alias1(5))

# this is just an ALIAS for function.. not the Name of Function .. def name_Funtion 
# simple python expression .. Not the LOOPS etc... 
# lambad can be used for the written expressions of returning several tuples values.. 


a= [i    for i in {4,3,2}]
print(a)

b = ( i for i in [1,2,3])

print(b)  # Generators types 
for i in b: 
    print(i)

for i in b:    # caN't print the SEVERAL Values of the Generator OBJECT's.  
    print("DDD")
    print(i)


# function is a Pythion OBJECTs.. IT can be passed as an ARGUMENT objects.. in the functions.. 
# memory efficients.. 

l1 = [34,2,344,90]

# def func1(*args):
#     for i in args: 
#         print(i)

# func1(*l1)

