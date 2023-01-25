import requests

import time

print(dir(requests))

t1 = time.time()
web_data = requests.get('https://www.w3schools.com/python/module_requests.asp')

print(web_data.text)

print(dir(web_data))
print(type(web_data))
time.sleep(2)

print(f" the time taken for REQUESTS Module is {time.time() -t1} seconds ")


import requests 

try: 

    r = requests.get('http://google.com')
    print(r.text)
    print(r.status_code)

except requests.URLRequired as ue: 
    print("Inside uRL Required")
except requests.exceptions.MissingSchema as e: 
    print(e, " RHis is inside the missing schemas")
except IOError as ie: 
    print(ie.args, "inside IOError")
except Exception as e: 
    print(e.args)
    raise e


value = { "name" : "ajay" , "marks" : [33,23,14,89]}
print(type(value))
print(value.get("name"))
print(value.get("one", 89))

r2 = requests.post('https://httpbin.org/post', data = value)
with open("new.txt","w") as f:
    f.write(r2.text)
    # f.write("#"*44\n \n")
    f.writelines("#"*44)
    f.write(str(r2.status_code))
print(r2.text)
print(r2.status_code)



