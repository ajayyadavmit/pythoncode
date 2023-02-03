''''
Method overloading CAN'T be achieved in Python.. like in C++, Java.. 
But with the other way we can achive the Method overlaoding in python.. 

When a class has two or more methods with SAME NAME but different BEHAVIROUS FUNCTION then it is method OVERLOADING in python. 

same method name >> But different method funtions >> method overlaoidng .. 
in python only Last method call will be there since older method will NOT be present 

Method overloaidng doe snot exits in python. But we can write the different LOGIC inside method so that method 
function's beHAVES in a different way to execute the code in the pythons. 

'''


print(locals())
# print(add(10,5))

class Add(object):

    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def add(self,z):
        return self.x + self.y + z 

a = Add()
a.add(4,3,4)