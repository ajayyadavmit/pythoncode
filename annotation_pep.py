# {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}

#  Annotations are for the better descriptions of the PARAMETERS in the function () and Class (). 


def add(a : int,b : int) -> int: 
    return a + b

print(add(5,4.4))
print((add.__annotations__))


''''
PEP 3107 – Function Annotations

Because Python’s 2.x series lacks a standard way of annotating a function’s parameters and return values, a variety of tools and libraries have appeared to fill this gap. Some utilise the decorators introduced in PEP 318, while others parse a function’s docstring, looking for annotations there.

This PEP aims to provide a single, standard way of specifying this information, reducing the confusion caused by the wide variation in mechanism and syntax that has existed until this point.

'''