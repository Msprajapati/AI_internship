num=int(input("enter a num"))
sum=0
while num>0:
    last_digit=num%10       #149   lstdig=9
    
    num=int(num/10)          #149/10 =14.9
    sum +=last_digit            #0+9

print(sum)    