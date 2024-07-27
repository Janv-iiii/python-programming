#WAP to accept 3 integers and print the largest of the 3 no. Make use of only if statement.
x=y=z=0
x=int(input("enter x:"))
y=int(input("enter y:"))
z=int(input("enter z:"))
maxx=x
if(y>maxx):
    maxx=y
if(z>maxx):
    maxx=z
print("Largest number is:",maxx)