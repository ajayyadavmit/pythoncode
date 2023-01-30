# Python Namespace will map one variable to one value. 
# Ensures that one variable will be Mapped to 1 value only. 

a = 50 
b = 30 
print(id(a))
print(id(50))
print(a, b)
print("#"*30)
a = 111
print(a)
print(id(a))
print(id(111))

# NAMESPACE WILL ensure only one name will be allocated in the Space memory in the Python.. 
# Types of Namespace 
# Built IN namespace >> Interpreter Starts >> dir()  >> gives the namespace variables. 
# GLobal Namespace  >> for the Moudle Level >> WHile program executes.. 
# local Namespace >> for the function variables.. 
# Enclosed Namespace >> inside the function >> namespace created for the Enclosed funtions.. 

# Built IN namespace >> when the Python INterpreter Starts then Built IN namepsace is used for the variables... 
# dir() is the function for the namespace 
# print(dir(lst))  # Gives the Local Namespace 
#Built In Namespace is there WHEN PYTHON INTERPRETER STARTS.. 
# GLOBAL NAMESPACE IS THERE when the python PROGRAM STARTS.. 
# NAMESPACE IS LIKE A DICTIONARY TYPE OF MAPPING FOR THE key- Value Pairs Objects.. 

# GLobal Namespace >> starts when the python Program is Started ... 

#  why Namespace is important ?  
# since you are working in Team, you have different module files. so even same variables created indifferent files, it wont confilit .. due to Namespace.. 

import os1

print(dir(os1))
print(os1.a)
# namespace are useful when several people works in a TEAM and creates a various Python PY file modules .. 


