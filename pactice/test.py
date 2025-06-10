# celicius to forenize 

a= float(input("enter temp in celsius"))

b= (9/5*a)+32
print("temp in fohrenheit", b)


#leep year
# Take year input from user
year = int(input("Enter a year: "))

# Check for leap year
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print(year, "is a Leap Year.")
        else:
            print(year, "is NOT a Leap Year.")
    else:
        print(year, "is a Leap Year.")
else:
    print(year, "is NOT a Leap Year.")



# calculator
A=float(input("enter first no.")) 
B=float(input("enter first no."))
print("press + for addition \n"+"press - for subtraction \n"+"press * for addition \n"+"press / for addition \n"+"press % for addition \n"+"press ** for addition \n")
ch=input("press")
match ch:
    case "+":
        print("sum", A+B)
    case "-":
        print("sub", A-B)        
    case "*":
        print("mul", A*B)        
    case "/":
        print("div", A/B)        
    case "%":
        print("mod", A%B) 
    case "**":
        print("exponesial", A**B)               
        