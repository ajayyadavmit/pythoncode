import oops

# __main__.Employee  # it tells here that this class Employee is defined in CURRENT MODULE only. 

class Employee: 
    def __init__(self, name,age) -> None:   # Magic Method of Constructor Types which is Called AUTOMATICALLY here in the Class callings. 
        self.name = name
        self.age = age
    def display(self):
        print(f"the name of person {self.name} and s/his Age is {self.age}")

e1 = Employee("rassfm", 457)  # Similar to calling like a functions.. 
# Now magic Mehtod is called Automatically Here with INIT() method callings. 
# self argument contains the Memory locaion of Object here. Object is passed in the self argument which stores the variables number here. 

print(e1)
print(e1.name)
print(e1.__dict__)  # e1 objectname.__dict__  () function contains the VARIABLE TYPES OF THE objects HOLDS.. 
e2 = Employee("hari", 908)

print(e2.display())
e3 = Employee("janakpur",890)
print(dir(e3))
print(e3.__dict__)
a = e3.__dict__
print(a['age'])
print(e2.__dict__)  # ATTRIBUTE of the variables... 
print(e3.display())
print(e3.__dict__)
print(getattr(e1,'name'))
