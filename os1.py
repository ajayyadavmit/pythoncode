import os
print(dir(os))
print(len(dir(os)))

print(os.listdir())
print(os.getcwd())
print(os.path.join('/Users/new','bijay'))

print(os.path.isdir('python project'))
print(os.path.isfile('test3.py'))

print(os.name)

import sys

print((sys.version))
# print(sys.copyright)
sys.stdout.write("Hellos")
print()
sys.stderr.write("Eroror here")
print()

a = ["dfdfd", "dfdfd"]
print(sys.getsizeof(a))

print(sys.argv)
