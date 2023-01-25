'''
inside the class function is called as METHODS. 
function are outside of the class 
Class name writte with Camel Case i.e First Letter of Word should be Capital Form. UseForm 
Constructors are automatically called when creating an Object of the Class. 
INIT() Function is used to create the CONSTRUCTOR for OBJECTS. 

Inheritance TYpes >> Hierarchical Inheritance ( from Parent to Child types )
Multi Level Inheritance types >> Inherit from various Class A, B, C to the Defined Class Types. 
Multiple Inheritance V/S Multi-LeveL Inheritances Factor's... 

FUnction with RETURN Can have capacity to STORE The values.. 
print command DOES NOT store any values. 
IT just shows the Values. 
REturn will STORE the values. 
Private Variables INSIDE the FUNCTION are written with DOUBLE UNDERSCORE __ . 
DOUBLE UNDERSCORE signifies the PRIVATE variables types. 
ENCAPSULATION property >> signifies the PRIVATE Variables and methods CAN'T Be accessed DIRECTLY in the Function (). 
INheirtance >> Multi - Level Inheritance  >> Multiple Inheritance  
DOuble Underscore __ value to signifies the PRIVATE Property Function's Values >>... 
OOP Features ( encapsulation, class , method, polymorphism )
Polymorphism >> Overloading vs Overriding Methods.. 
super() function () would help to call the PARENT function ().  Super().functionname() pass to the Parent CLASS for calling. 
super().function_name() >> would help to CALL the Parent Function
super() function call . DOT . FUNCTION NAME () >> Helps to Calls the Parent Function Values...  

OOP Concepts Includes the 
>> CLASS & METHODS ( methods are inside the FUNCTION defined inside CLASS)
>> Getter & SETTER methods ( have access to the PRIVATE Variables with DOUBLE UNDERSCORE Symbol  __onevalue, __twovalue)
>> Polymorphism ( Same Function name but with different ARGUMENTS )
>> Overloading and OVerriding arguments in functions ( Multiple inheritances)
>> Inheritances Types >> Multiple &&  Multi_LEVEL inheritances types...  
>> Encapsulation function ( Does not allow to access the PRIVATE Variables.. )

super() is a especial function used for callign Parent Methods. with super() you need to specify which function 
actually you want to Call for it .. 

PRINT() FUnction >> always Print the RETURN TYPES vlaues .. if no vlaue Returned then NONE will be PRINTED... 
'''


b = "one"
print("with value b "+b+" fiod")

class Fruit:
    a = "mangoes"
    __onefruit = "Private variables in FRUIT class"
    __namefruit = ""
    def __init__(self) -> None:        
        print(f" inside the Fruit Class " + self.a)
    def getFruit(self):
        print(f"Accessing PRIVATE Variables {self.__onefruit} ")
        return self.__onefruit, self.__namefruit
    def setFruit(self,v2):
        self.__namefruit = v2
    def totalFruit(self, a1, a2):
        return a1 + a2 
    def displayKiwi(self):
        print(">>"*5)
        return " vlaue in FRUITS FRRF INSIDE"

class Orange():
    place = "Kathamndu"
    def __init__(self) -> None:
        print(f"inside the Orange Fruit at {self.place}")
    def totalFruit(self):
        return "inside Orange" 



o1 = Orange()
print(o1.place)

print("$"*44)
f1 = Fruit()
print(f1.getFruit())

print("$"*44)
f1.setFruit("CUP FRUIT") ;  print("#"*33)
r1, r2 = f1.getFruit()
print(f1.getFruit())
print(r1,"#### >>>>", r2)

class kiwi(Fruit, Orange):
    def __init__(self) -> None:
        print(f"{self.place}")
        print("Value of fruit   " +self.a)
        print("place value   " +self.place)

    def totalFruit(self, a1, a2,a3):
        # super(self.a1, self.a2)
        return a1 * a2 *a3
    def displayKiwi(self):
        print(" vlaue in kiew")
        a5 = super().displayKiwi()
        print(a5)
        return "ANYONE LIFE"

k1 = kiwi()
print(f1.totalFruit(5,8))
print("$"*33)
print(k1.totalFruit(5,4,5))
print(k1.displayKiwi())



l = [34,56,90,"sdfkf"]

for v,n in enumerate(l, start=4):
    print(v,n)
    if type(n) == str: 
        print(n)
        for i,e in enumerate(n, start=3):
            print(i,"  ###  ", e)

m = dict()

s = set()
r = range(4)
print(m,s,r)

if type(s) == set: 
    print(s, "is o type SET")

print("alb") ; print(45+55) ; print("ram")  # one line writing python commands types.. 

del s 
print(locals())


