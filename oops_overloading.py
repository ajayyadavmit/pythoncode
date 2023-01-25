
# Overloading concept is Function name is same but the Paramerter is differet. So the output will be different 
# depends upon paramters of function.. 

class Ws():
    def displayname(self, name =''):
        print("welcome to ajay" +name)

ws1 = Ws()
print(ws1.displayname())

print(ws1.displayname("RRAAAMM BHAWANI"))

# here same funtion name is there but called with different Argument types of Variables in Function. 
    
def totallingValue(a, b = None, c = None):
    if (b is not None and c is not None):
        return a + b + c 
    elif (b != None):
        return a+b
    elif (c != None):
        return a + c 
    else: 
        return a 

print(totallingValue(3,4))
print(totallingValue(13,14,45))
print(totallingValue(390))





# OverRidding Concept ( Always Comes in the Class Format's >>)
# used in the Class Inheritance Concepts. 

print(locals())   # shows the local Function name () variables Stored in the Memory 

# DEFINING SAME FUNCTION NAME WITH DIFFERENT ARGUMENT IS NOT PERMITTED IN PYTHON as Compared with C++ / Java. 

class CopyBook():
    def cb(self, a,b):
        print(f" value is {a}  and {b}")

    # def cb(self,a):
    #     print(f" the vlaue {a}")

    # def cb(self, a,b,c):
    #     print(f" {a}  and {b} and {c} values Has There")

cb1 = CopyBook()
# cb1.cb(5)
# cb1.cb(4,"dfkf")

'''Why no Function Overloading in Python?

Python does not support function overloading. When we define multiple functions with the same name, the later one always overrides the prior and thus, in the namespace, there will always be a single entry against each function name. We see what exists in Python namespaces by invoking functions locals() and globals(), which returns local and global namespace respectively.'''

