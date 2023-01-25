# pickle library helps to USE the file for the SERIALIZATION activity file write method & to Read file data for the Deseriabliaton 
# activity in pickle format 


# pickle dump function. pickle libarry module isthere  object file, list / dictionary/ set etc...  
# write data in file / mode = "wb" write in Binary Form data ... 
# data is stored in Serilized format in the Binary form mode data ...  

'''
PICKLE Module in Python helps to SERIALIZE ( STORE)  and DESERIALIZE ( READ) data from the FILE system in python. 

SERIALIZE >> STORE DATA inside the FILE 

DESERIALIZE >> RETRIEVE OR Read Data from the FILE> system's. ..

pickle has 2 methods 
dumps >> dump in SERIALIZE object 
Loads >> Read data from the FILE.. 

pickle has  2 mode only (wb >> write in binary format mode) 
( rb >> read in binary format mode data )

Pickle in Python is primarily used in serializing and deserializing a Python object structure. In other words, it's the process of converting a Python object into a byte stream to store it in a file/database, maintain program state across sessions, or transport data over the network.

JSON is a text serialization format (it outputs unicode text, although most of the time it is then encoded to utf-8), while pickle is a binary serialization format;

JSON is human-readable, while pickle is not;
'''

import pickle 

s = {4,4,3,5,6,89,909}

print(type(s))

pwrite1 = open("oofile.txt","wb")
pickle.dump(s,pwrite1)
pwrite1.close()

pread1 = open("oofile.txt","rb")
print(pickle.load(pread1))
pread1.close()

