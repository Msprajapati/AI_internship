null_set=set()
set1={9,22,11,2,5,4,4,9,8,7,6}
print(set1)
set1.add(9)
set1.add(11)
print(set1)

set1.remove(11)
print(set1)

print(len(set1))
#set1.clear()
print(set1)
print(set1.pop())
print(set1.pop())

set2={"ram","shyam","krishna","jay","veer"}
print(set2.pop())


set3={1,12,4,5,13,58,45,55,4,2,3,}
print(set1.union(set3))
print(set1.intersection(set3))
 