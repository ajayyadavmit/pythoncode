
'''
> Random gives the value from the random value from the list , tuples, random 
> random module 
FUnctions lists:: 

random.randint(start, stop values)  >> GIves Values WITHIN Range values. 

random.randrange( Start , stop -1 value)  >> Similar to the Python RANGE() FUNCTION Range(0,9) 9 is NOT included. 

'''
# important function of random module Randint() random.random() randrange() random.uniform() random.shuffle() 

# import random 

# print(dir(random))

# print(random.randint(3,9))

# print(random.randrange(3,9))


# print(random.choice([33,44,2,6,4,23,89,12,98]))


# print(random.random())
# s = [34,56,23,89]
# print(random.shuffle(s))

# print(random.uniform(3,9))

# print(random.randint(3,9))
# print(random.randrange(3,9))



# print(random.random())
# print(random.uniform(3,8))

# random.shuffle(s)
# print(s)



print("Test")

import random as r 

print(r.randint(5,9))

print(r. randrange(4,6))
print(r.random())

l = [23,55,11,24,89,77,48]

r.shuffle(l)
print(l)

print(r.choice(l))
print(r.uniform(3,6))


