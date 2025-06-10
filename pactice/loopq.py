#no. 1 to 100

# i=1
'''
while i<=100:
    print(i)
    i +=1

j=100
while j>=1:
    print(j)
    j -=1
'''

#a= int(input("enter a no. for table")) 
# while i<=10:
#    # print(a*i)
#     i +=1  


# idx =0
# list = [1,4,9,16,25,36,49,64,81,100] 
# while idx <=10 :
#     print(list[idx])
#     idx +=1


'''
nums=(2,5,7,8,9,12,15,45,65,98,23,25,75)
x=45
i=1
while i<len(nums):
    if(nums[i]==x):
        print("found",i)
        break
    else:
        print("finding")
    i +=1   
'''

'''

i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i +=1
print("end of loop")
'''






'''
i=0
while i<=10:
    
    if(i%2==1):
        i +=1
        continue#skip
    print(i)
    i +=1
'''


### for loop
'''
list = [33,22,23,21,34,43,54,65,45,35,63]
x=10 
for val in list:
    if(x==val):
        print(x,"index of list",)
        print(list.index(x))
        break
else:
    print("not found")
    
'''

#range()
'''
for i in range(10):  #start from 1 and ends with 10
    print(i)

for i in range(1,10): ##startin and ending
    print(i)    

for i in range (1,10,2):### starting , ending , and step
    print(i)    
'''

# some of n numbers

# n= int(input("enter n "))
# sum=0
# for i in range(1,n+1):
#     sum +=i
# print(sum)


##facotorial of the given no.
'''
n= int(input("enter n "))
fact=1
for i in range(1,n+1):
    fact *=i
print(fact)
'''


num=int(input("enter a no"))
i=1
fact=1
while i<num+1:
    fact *=i
    i +=1
print("factorial ", fact)    













