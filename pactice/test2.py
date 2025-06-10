def primeno():
    num = int(input("Enter a number: "))
    if num < 2:
        print(num, "is NOT a prime number.")
    else:
        is_prime = True
    for i in range(2, num):
        if num% i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, "is a Prime Number.")
    else:
        print(num, "is NOT a Prime Number.")
   
primeno()

#sum of digits
n=int(input("some of digits till"))
i=1
while i<=n:
    i +=1
    print(i)



#factorial 

#star pattern

#no of student data , name grade schoolname ,id ,, check students data by id in dictionory