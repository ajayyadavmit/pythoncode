# iterator vs Iterables function in Python 
# list [] tuple () dictionary {} set {} range () all are iterables in Loop

# for loop is INDIRECTLY Calling the ITER() and NEXT () functions inside. 

number = [4,3,2,5,89]  # Iterables 

# for i in number:
#     print(i)

# print(dir(__builtins__))

for i in dir(__builtins__):
    if i == "next": 
        print(i)


num_iter = iter(number)
print(next(num_iter))
print(next(num_iter))
print(next(num_iter))
print(next(num_iter))
print(next(num_iter))

print(next(num_iter))
