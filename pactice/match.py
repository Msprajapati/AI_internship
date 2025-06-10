# def check_number(y):
#     match y:
#         case 20:
#             print("its 20")
#         case 30:
#             print("its 30")
#         case _:
#             print("neither 20 or 30")    

# check_number(20)
# check_number(30)
# check_number(10)               

a= int(input("enter a no."))
b= int(input("enter a no"))
print("press + for addition \n" + "press - for subtration\n" + "press * multiplication \n"+ " press / for division")
ch= input()
match ch:
    case "+":
        print("sum",a+b)
    case "-":
        print("sub",a-b)
    case "*":
        print("multi", a*b)
    case "/":
        print("division",a/b)
    case _:
        print("invalid input")            
