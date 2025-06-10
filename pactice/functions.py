'''
def sum_calculate(a,b):
    sum= a+b
    print(sum)
    return sum 

sum_calculate(10,54)
sum_calculate(123,345)

def print_hello():
    print("hello world")
    print("by functions")

print_hello()
'''

'''
cities =["jodhpur","kota","sikat", " churu", "pali","jaisalmer","bikaner"]
states=["rajasthan"," delhi","mp", "up", " bihar" ,"gujrat"]

def print_len(list):
    print(len(list))

# print_len(cities)    
# print_len(states)

def print_inline(list):
    for item in list:
        print(item, end=" " )

print_inline(cities)
'''

#find factorial of n, n is perameter
'''
def fecto(n):
    i=1
    fact=1
    while i<=n:
        fact *=i
        i +=1
    print("factorial",fact)    

        

fecto(3)
'''

'''
def usdtoinr(n):
    inr = n*85.57
    print(n,"dolor in inr", inr)


usdtoinr(2)
'''

#input no using func , print odd or even as string
def evenodd():
    n=int(input("enter a no."))
    if(n%2==1):
        print("odd")
    else:
        print("even")    

evenodd()
