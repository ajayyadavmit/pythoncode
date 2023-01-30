## Range Function () with the DEFAULT POSITIONAL ARGUMENTS IN THE FUNCTION (). 
# Range is often considered as the Python MISTRY function in programming languages. 
# Default Value >> Positinoal Argument  >> Key -- Value arguments.. 


def func(a, b= 5, c = 10):
    print(a+b+c)

func(5)  # only a value will be Given here .. 

func(5,10)  # here A, B value's are Given.. 

func(5,5,5)  # Defualt Values are NOT Given. 

# range function is a BUILT in CLASS that executes in-built the COnstructors method. 

# range(10)  # is the class that calls the inbuild Constructor methods.. 

# # syntax 
# range(start, stop, step value)


def range1(start=0, stop = None, step = 1):
    if stop is None:
        stop = start
        start = 0
    # print(start)
    while (start < stop):
        print(start)
        start = start + step

range1(15)

#  Range Functions () in Python   z####