
# Comprehension is the Short hand way of defininig the LIST dictionary functions. 

print([ x   for x in "abc"])

print({ y: y+"sdf"  for y in "mangoes"})

value_set = {4,4,3,8,90,4}
value_set2 = {90,4,55,78,91}

print(value_set)

value_set.add(56)
print(value_set)

print(value_set.union(value_set2))

print(value_set2.intersection(value_set))

print(value_set.difference(value_set2))
