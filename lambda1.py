# lambda or anonymous function >> function having NO Names is Lambda function ()

# def add(x,y):
#     return x+y

# print(add(4,5))

# lambda arguments : expression   # lambda function can take any number of arguments but returns only ONE Expressoin value 

# a = lambda  x,y,z:  x+y+z 
# print(a(4.5,5,3))

# ZeroDivisionError("dkfkf ")


# l = [34,23,56,88]

# def l_value(*l):
#     for i in l:
#         print(*l)
# l_value(l)

# lambda functino any arment : but one expresson 

# lambda x,y,z : x -y -z 


# l2 = [[4,89],[78,34],[33,98]]

# l2.sort()
# Normal function can be used with LAMBDA Functions here >> 
# def a_first(l2):
#     return l2[1]
# l2.sort(key=a_first)

# l2.sort(key= lambda x : x[1])   # through LAMBDA Function for the SORTING order applies here 

# print(l2)

# value1 = lambda x,y : x*y + 10

# print(value1(5,5))


# l4 = [33,45,89,65]

# def list_value(*args):
#     for i in args: 
#         print(i[2])

# list_value(l4)

# lambda is the anonymonous (no named function) that takes syntax :  lambda argument (n no's of argument): expressions 

a = lambda x,y,z : x + y + z 

print(a(5,4,7))

l1 = [34,67,234,89]

y = lambda l1 : sum(l1)

print(y(l1))

s1 = " this is good boy where you can find in Nepal"

s2 = 678

y = lambda x : x.upper()
print(y(s1))

print(type(s1))
print([ x   for x in "abc"])

for x in "abc":
    print(x)
    if x == "b":
        continue
else: 
    print("ELSE in FOR")

y1 = [2,4,5,6]
print([ x   for x in y1 if x %2 != 0 ])

# lambda arguments : expression Retun value 
x,y,z = 2,3,4
print((lambda x,y,z :  pow(x,2) + y + z) (x,y,z))


def square(a):
    return a * a

print(square(5))

print(list(map(square, y1)))

print(list(map( lambda a: a*a  , y1))) #! this is the map fuunctin with LAMBDA for the SQUARE Value's. 

def cube(a):
    return a*a*a

print(list(map(lambda a: a*a*a, y1)))

print(list(filter(cube, y1)), "Filter values")

marks = {"ajay" : [34,55,67], "aman" : [34,55]}

m1 = [34,55,78,98,674,2,1,3,4,9]

# def value_gt(*args):
#     # print(args)
#     for i in args: 
#         if i > 5:
#             return True

# # print(value_gt(*m1))

# print(list(filter(value_gt, m1)))
print("#"*44)
print(list(filter( lambda x : x >5, m1)))

from functools import reduce

# reduce(funtionna e, sequence iterables to reduce the values )
m2 = [2,3,2,2]
m3 = ['abc','def','ghi']
print(reduce( lambda x,y : x +y, m3))
# Reduce does the cummulative arithmetic operations in the functions ().



# ! SHorthand Lambda function 

'''
a = lambda x : x**4

[a(e) for e in [1,2,3,4,5,6,7,8]]


map(lambda x: x**4, (1,2,34,5,6,8))


print([ (lambda x: x *x) (x)    for x in [2,4,8,5]]) #! Lambda function CALL syntax 


print([ x + "1111" for x in "amnop"])

print([ (lambda x : x +"1111") (x)  for x in "abcdef"])  

'''

l1 = ["45","55","45","55","45","55"]
print(type(l1))
for i in l1: 
    print(type(i))

print(list(map(int,l1)))

print([(lambda x: x +5) (x)  for x in  list(map(int,l1))])  # ! this is the Map and Lambda Functions usages. 

s1 = set(l1)
print(s1)
print(l1)

print(tuple(map(tuple, l1)))

num = [5,6,3,9,4,0.5,1.8,6]

#! this is making the SQUARE Number 
def square_num(a):
    return a *a 

print(list(map(square_num, num)))
print("#"*45, list(map( (lambda x: x*x*x )  , num )))

def cube_num(a):
    return a*a*a

value_func = [square_num, cube_num]
#usage of the Map FUntion with Lambda , Map calculates to Function and Iterable objects. 
for i in range(6):
    print(list(map(  lambda x: x(i),  value_func)))

def value_greater(a):
    return a <5
b=33
print(value_greater(b))

# filter function can be used with the Filter(functionname(), Iterable Objects >> LIST [] data types)

print(list(filter(value_greater, num)))

# filter funcction filter the values,  Map funtion works on the iterables objects, Lambda function works as 1 line Parallel arguments, Exceptions handling are of Modules types Exceptions Updated >>

from functools import reduce

list3 = [1,2,3,4,5]
print(sum(list3))
print( reduce(lambda x,y : (x+y), (list3) ) )

# Reduce Function will do the Cummulative summation fo the Values from the 1st index number. 
import math
print(math.ceil(5.6))

#Map Reduce Filter Functions.  MAP calculates values in ITERABLE form Functions, 
# Filter() gives the filter results in TRUE / False Form 
# Reduce (functools) will do the CUMULATIVE Summation Factors. 
# l = [4,5,8,9,11,13]  4+5 = 9 + 8 = 17 + 9 = 23 

