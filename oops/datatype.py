'''
Data type si the category of the data.  Here all the values of data are in Object format. 
x = 10 >> 10 is an object format. 
Dat Types 
Numeric type:  INT, FLOAT , COMPLEX
text type :  STRING ( there is no Character data type)
sequence type:  List, Tuple, Range
Mapping type:  Dictionary ( key : Value Pairs () format)
Set type: Set, FrozenSet 
Boolean type: bool 
None Type:  None 
'''

'''
INT DATA TYPE: 

int can be of any Length.. It depends upon RAM of copmuter for the Storage. 
##############
FLoat Data type >> can be accurate for the 15 Decimal Places.. 
Exponential is part of Float numbers.. 2e7 >> e >> 10 to power to (7) number 

'''

print((11,000))  # output is INT Class INT type
# COmmad is used for the WHITESPACE in Python.. So you Won't be able to see COMMA sign in Numbers. String formating is required 
# now use the variable for Storage of values. 
x = -11

print(12.2324234324234234237e4)  ##Float number with Exponential Data Types.. 
# e is used for exponential.. Scientific notations.. 

'''
Complex Number :   a + bj  ( a, b can be integer or Float Part ) >> bj is IMaginary Part 
# j should be used as Keyword for the Complex Data Types in the COMPLEX number... 

'''

print(type(2 + 3j))
print((2 + 3j)*3)  
'''
Text Types >> String / Char 
Char is not in pYthon data types.. 
String is a Sequence of character.. Enclosed in Quotes.. Single Dobule Triple quotes.. 
for character data type  >> it can be used with 1 String value data types. 
string INDEXING >> positing values. >> Positive +Ve INdexing   >>  -ve Indexing also 
Python supports both Indexing +ve or -ve format fron S to End && End to Start.. 

LIst [] 
List is collection of different DATA TYPES... list can be collection of integers, string or mix types. 
list can be ordered. u
list is Mutuable (changeable) >> list can be Changed.. it is sequence of ATOMs.. AToms can be any data types. 

Tuple ()  collection of data types.. Tuple is IMMUTABLE.. Can't be changed in Tuple.

Dictionary {}  Unordered Data Types.. SO indexing cant be used.. Unordered Data types.. 
Can be acessed with KEY value Pairs.. KEY data types can be used to access VALUES.. 
{a:45, "b":45}

Set {} 
> unordreed collectons of unique atoms.. separate by COMMA.. 
atoms are not in ordered so it can't be accessed with INDEX's. 
SET are unique data types.. No repetition data types in SET.. 

Range() 
> Immutable Sequence no from Start to ENd with STEP Number.. STEP number is defualt by 1, Start is defuatl to 0. 

Bool >> vlaues True or False ( Determine the Conditinal Statement )

None >> Data Type that does not contatins ANY value.. 
If Object Does not exits then NONE type data. 
if there is no Object then give the NONE type None type.. None is of type NULL in the other languages.. 

None Data Type value assignment if no value is there ... IN programmng it is used more for structured approach. 
'''

s:str = "Nepal"
print(s[3])
print(len(s))
print('''one
two
three''')  ##
print(s[3])

d = {"ajay": 455}
print(type(d))
print(d["ajay"])

s1 = {33,3,3,4,4,21,45,89}
print(type(s1))
print(s1)
for i in s1: 
    print(s1)


a = None
print(type(a))

if a: 
    print("eh")
else: 
    a = 5
    print(type(a))

'''
How Python WOrks ?
Python uses both Compiled & Interpreter language.. 
1st write python source code .. Save with .py extension file. 

2nd >> Give python source code to the >> COmpiler .. 

3rd >> Compiler CONVERT's  to >> BYTECODE >> .PYC PYC BYTECODE.. 

COMPUTER does not understand the PYC code .. it understands only the Machine COde lnaguage ( 1/0)
SO now the PVM Python Virtual Machine converts the bytecode to the machine code using the INTERPRETER python. 

.py >> pyc >> Conmpiler >> bytecode >> pvm >> interpreter >> Interpreter 
Thus we need both Compiler and Interpreter.. 

Why we need BOTH ? COmpiler / Interpreter.. 
Interpreter >> Portablity is there with Interpreter.. 
Compiler >> SPeed is Fast.. 

Cpytion >> C languge python. 
Jpython >> Java lang

Python is compiled interpreted language.. It uses both compiler , interpreter .. 
python is refered as Compled Interpreter langugage. 
'''