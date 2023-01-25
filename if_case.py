
# if condition should be written with cautions since lower condidtions are not executed if Upper COnditons are MET directly in format. 



lang1 = input("Enter value ")

match lang1:

    case "a": print("Has vlaue ")

    case "b" : print("BBBBB")

    case "c" : print("CCCC")

    case _ : print("Default Values Here LISTED inside >>>")

''' Always Write the IF ELSE Condition from TOP to BOTTOM approach otherwise the last ELSE conditions 
can't be Executed Well
'''

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

