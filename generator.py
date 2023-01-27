# generator are iterators 

# iterable >> are LIST, TUPLE, STRINGS
# iterators >> MAP() returns an Iterators,  >> for() returns an Iterators

l = [1,2,3]  # iterable

i = iter(l)  # converts list into ITerator object with ITER() function.
print(type(i))

#Now this ITerator object will work with NEXT() function to get the Next ITEM in a LIST value.
print(next(i))

# next(l) # can't call the Iterables  >> gives ERROR ::  'list' object is not an iterator

#  For Loop () will work on that basis for ITerable and ITERATORS object's...

# GENERATOR ARE ITERATORS
#  GENERATOS  generate AT ONE TIME ONLY ONE 111 NUMBER.
# MEMORY BENEFITS IN THE PROGRAM 
name= "23432432"

print("s\tkd\"fk\"f" + "dfdf   " +name + "    dfkdf")   

# CREATE A GENERATOR FUNCTION 

# 1. GENERATOR FUNCTION 
# FUNCTION THAT TAKES 1 ARGUMENT AT ONE TIME, >> PRINT 1 TO 10 AT ONE TIME. 


def numberGenerate(n):
    for i in range(1,n+1):
        yield(i)   # print(i)

num2 = numberGenerate(10)

##Now you can create a Generator that iterable in the Demand Basis >> instead of print () use the Yield() keyword 
# yield keyword .. >> Yield keyword would generate on the demand basis.  no need to write () parenthesis. 

print(type(numberGenerate))  # Even GENerator are function that Generates the Number. 

for num in numberGenerate(5):
    print(num)

# who is demanding the nuber >> its FOR loop 
# if you run the for Loop Again , >> then you cannot get the number since it is NOT in memory. 

for num in num2:
    print(num)

print("#"* 45)
for num in num2:   #here the number can't be printed since it is not stored in memory. 
    print(num)

# generator can be converted to the LIST data type . 

num3 = list(numberGenerate(5))

print(num3)

# 5 >> 2, 4 
# def evenNumber(n):
#     while (n>0):
#         if n %2 == 0:
#             yield n
#         else: 
#             n = n-1 

def evenNumber(n):
    for i in range(1,n+1):
        if i % 2 == 0:
            yield i

en = evenNumber(5)
print("dkfkfkfkf")
for v in en: 
    print(v)

for v in en:   #again there is no Values in the Generator functions.. 
    print(v); print(">>>")

# Generated number from the FOR loop for ( ) loop.

# Generator Comprehension  like LIST comprehension. 

l4 = [3,4,5]
l4_value = [ i*i   for i in l4]

print(type(l4_value))
l4_value_new =  (i*i   for i in l4)  # this is generator NOT the TUPLE data types. 


print(l4_value_new)

for i in l4_value_new:
    print(i)

for i in l4_value_new:
    print(i,"$$$")

for i in l4_value:
    print(i)

for i in l4_value:
    print(i,"$$$")

# TUple comprehension are the Generator Types of Data Types.  

import time 

# t1 = time.time()
# l = [ i  for i in range(10000000)]
# t2 = time.time()
# print("time value for List " , (t2 - t1) )

# with open("1gen.txt","w") as f: 
#     for i in l: 
#         f.write(str(i))

t1 = time.time()
l =  (i  for i in range(10000000))
t2 = time.time()
print("time value for List " , (t2 - t1)*1000 )
for i in range(11):
    print(next(l))

for i in range(11):
    print(next(l))

for i in range(11):
    print(next(l))

for i in range(11):
    print(next(l))