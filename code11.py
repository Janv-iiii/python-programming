#WAP to test the divisiblity of a number with another number.
n1=int(input("enter n1:"))
n2=int(input("enter n2:"))
remainder=n1%n2
if(remainder==0):
    print(n1,"is divisible by",n2)
else:
    print(n1,"is not divisible by",n2)