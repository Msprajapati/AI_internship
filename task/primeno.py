num=int(input("enter a number "))
if num<2:
    print("its not a prime no ")
elif num>1:
    for i in range(2,num):
        if num % i==0:
            print("its not a prime number")
            break
    else:
        print("its prime number")
