import os
print(os.getcwd())

# os.chdir('/python project')

print(os.getcwd())

# f = open("os1.py","r")
# print(f.read())
# f.close()

a = os.path.join('/Users/ajay/Desktop/Django/2. htmlproject','python project')
print(a)
os.chdir(a)
print(os.getcwd())
print(os.listdir())

mystr =  "this is new one "

print(type(mystr))

import json

# json file does not have Comments values. Json file has DOUBLE quotaitons only. 

data = '{ "name" :"Ravi", "marks" : 54 } '

parsed = json.loads(data)
print(data)
print(parsed['name'])   # data accessed with Key Value Pairs .. 

data2 = {
    "cars"  : ["tyoy", "ferrair", "cruise"],
    "year" : [22,23,24],
    "freeze" : ("rt", 45),
    "Value" : False
}

# Dictionary to JSON for javascirpt 

# json .dump for javascripts compatible values.. 

value = json.dumps(data2)
print(value)

# TUple is converted to the ARRAY Values in the JSON. 

'''
List >> flexible type of data type .. 

Python has array module >> ordered collection of data types.. Fixed Data Type in the python programming type. 

## data science for using the Numpy Array >> C Bindings .. Performance Fast .. for python .. 

Python Bridge with C language..  
Performance  like C lang. 

Flexibity like Python Language.. 

list vs String ... 

List are Mutable.. 
String are NOT Mutable.. Not Changeable types... 

'''

s = "one"

a = s.title()

print(s)