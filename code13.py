#Making a Basic calculator
n1=int(input("enter n1:"))
n2=int(input("enter n1:"))
operator=input("enter any operator:")
if operator=='+':
    print(n1+n2)
elif operator=='*':
    print(n1*n2)
elif operator=='-':
    print(n1-n2)
elif operator=='%':
    print(n1%n2)
elif operator=='/':
    print(n1/n2)
elif operator=='//':
    print(n1//n2)
else:
    print("No such operator found")