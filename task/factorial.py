def facto():
    n=int(input("enter a no"))
    i=1
    fact =1
    for i in range (1,n+1):
        fact *= i
        i +=1
    print(fact)
facto()