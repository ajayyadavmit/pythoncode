
'''
json is used to take data from the website in the Javascript format ES6 Language. 
json does not Support COMMENTS 
json should use always DOUBLE QUotations "" values only. 

python Dictionary to JSON value conversiont to Javascript websites function name #  json.dumps()  json.dumps()  function

from the Javascript to Python value conversion ..  
Load in the String Formats from the third party data 
string value represented as ''  single quotations marks 
function name # json.loads()   # json.loads()    >> from Website to python objects.. 
json.dumps()  # from the python Dictionary datatypes to the ES6 Javascript objects. 

in the browser Backticks is used for the Javascript objects. ``
json array [] list type in python 
json object {}  dictionar type in python 
for the list access, you use index number  ,  
for the dictionary access, you use the KEY "key" pairs in the coding. 


import json

data = 
{
    "name" : "ajay",
    "address" : "kathmandu",
    "fruits" : ["mango", "orango", 56, "papaya", 89,99,123],
    "marks" : [34,55,12,23,24,56],
    "course" :{
        "1stSemester" : ["leadership","diversity", "AcademicWriting", "Policy"],
        "assessmentTypes" : {"leadership" : "Formative", "AcademicWriting" : [45,55,89]}
    }
}

print(type(data))
print(data)

data2 = json.loads(data)
print(data2)
print(type(data2))

print(data2["course"]["assessmentTypes"]["leadership"])

course = {
        "1stSemester" : ["leadership","diversity", "AcademicWriting", "Policy"],
        'assessmentTypes' : {"leadership" : "Formative", "AcademicWriting" : [45,55,89]},
        "isStudent" : True,
        "isFirst" : False
    }

# json vs XML data types
# XML data types takes lot of SPaces due to <>  & </> tags. Json is Lightweighted 
# since it does not include tags and Clean Code. 
# <1stSemester> "leadership","diversity", "AcademicWriting", "Policy" </1stSemester> #XML Tags Types here. 

print(type(course))

course2 = json.dumps(course)

print(course2)

book = {}  

book["science"] = 350
book["math"] = 678

print(book)

# dumps  >> "S"  stand for STRING values. 

# loads >> "s "  stand for STRING Value. 

for value in book: 
    print(book[value])

'''

from json import loads, load, dumps, dump
# print((json.__doc__))  # can't be accessed DOC method since we use the IMPLICIT method here 



course = '''{
        "1stSemester" : ["leadership","diversity", "AcademicWriting", "Policy"],
        "assessmentTypes" : {"leadership" : "Formative", "AcademicWriting" : [45,55,89]},
        "isStudent" : true,
        "isFirst" : false
    }'''

print(type(course))

import os , sys 

course_json = loads(course)
print(course_json)

print(type(course_json))

course_dump = dumps(course_json)
with open("jsonnew.json","w") as f:
    f.write(course_dump)


with open("jsonnew.json","r") as f: 
    a2 = load(f)
    print(type(a2))
    print(a2)


newdata = {
    "name" : "ajay",
    "address" : "kathmandu",
    "fruits" : ["mango", "orango", 56, "papaya", 89,99,123],
    "marks" : [34,55,12,23,24,56],
    "course" :{
        "1stSemester" : ["leadership","diversity", "AcademicWriting", "Policy"],
        "assessmentTypes" : {"leadership" : "Formative", "AcademicWriting" : [45,55,89]}
    }
}

print(type(newdata))
print(newdata)

f2 = open("jsonnew.json","w") 

dump(newdata,f2, indent=4)
f2.close()

# dump method writes to the file in the Dictionary Format {}
# dumps method will give the output in the JSON JS notation format.

# dump(objectCOnsideringVariables, FileToWriteOutput, indent = 5)

# load(load from the file )

with open("jsonnew.json","r") as f: 
    val = load(f)
    print("*"*55)
    print(val)
    print(type(val))

