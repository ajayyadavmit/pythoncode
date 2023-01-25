'''
OS - The OS module in Python provides functions for interacting with the operating system. OS comes under Python's standard utility modules. This module provides a portable way of using operating system dependent functionality. ... path* modules include many functions to interact with the file system.

Sys - The sys module in Python provides various functions and variables that are used to manipulate different parts of the Python runtime environment. It allows operating on the interpreter as it provides access to the variables and functions that interact strongly with the interpreter.
'''

import sys
print(sys.version)


# module >> is not Self Contained program. Module is designed to be imported in file and run. WHereas the Program is supposed to run Self. 

# import math1

# math1.mabc()

# math1.cj()
# print("#" *22)
# print(dir(math1))

import os 
print( os.path.join("kk","78join"))
print(os.getcwd())

a = os.path.split('/Users/ajay/Desktop/Django/2. htmlproject/python project')
print(type(a))
print(a, len(a))

for i in a: 
    print(i)


# os.path.join()
# os.path.split()


import json
a = '{ "name":"Ajay", "marks" : 435}'

a2 = { "name":"Ajay", "marks" : 435, 'present': True }


print(json.dumps(a2))

print(json.loads(a))