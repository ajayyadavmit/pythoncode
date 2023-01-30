Memory Management in the Python AUTOMATIC ..  

Python memory manager >> Allocation of Memory 
Python Deallocation of memory >> Python Garbage Collector >> De-allocation  () 
Garbage Collection >> Deallocation of Meory 

Stack memory >> Static Memory  ( can be accessed Directly.... )

Heap Memory >> Dynamic Memory ( cant access directly )  >> accessed by use of References Variables... 

There are two types of memory 

a. stack Memory >>  GLobal Referecen, Function name, variables. ( allocated by Compiler COmpiler Software)
b. Heap Memory >> for Objects types..  ( allocated by Interpreter Interpreter software )

.pYC FIle then Interprerter takes the files.. 


Stack memory at the COmpile Time.. 

Name of variables, Functions, defined and tagged there.. 

Dynamic or Heap Memory 
# Assignment Variables Values is defined there 
for example - x = 10.. 10 value is assigned to the x on the HEAP Memory Time Values. 

this is all done through OBJECT alloations.. 
x = 10 + 20 
x = 30 ( object and Tagged to the x variables at Static Time. )

2 times memory allocation 1. Compile Time..  2. Runt time >> Interpreter ..  

after functions executions, >> by Garbage Collector  >> Memory is Destroyed in the program. 

Garbage Collector is the program that removes which has no Referencing Values in the Python. 

2 Algorithm for the Garbage Collectors are a. Reference Counting    b. Tracing ... 


refence counting  x = 10, y = 10 ..  2 reference are ther for ojbect 10.. 

reference count = 0  then Garbage Collector script Call to the Conditions.. Then it Removes the Object from the Memory.. 

Garbage Collector script will run when the reference count is 0.. 

what is disadvantge of Garbage Collector ?

Execution Overhead >> coutner update internally... 
Memory fo the allocations in counter.. 





