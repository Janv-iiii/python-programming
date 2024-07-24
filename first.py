#Making basic python calculator
a=int(input("enter a no. a:"))
b=int(input("enter a no. b:"))
operator=input("enter any operator:")
if(operator=='+'):
    print(a+b)
elif(operator=='*'):
    print(a*b)
elif(operator=='-'):
    print(a-b)
elif(operator=='/'):
    print(a/b)
elif(operator=='%'):
    print(a%b)
elif(operator=='//'):
    print(a//b)
else:
    print("No such operator found")