#Program to display a menu for calculating area of circle or perimeter of a circle.
radius=float(input("enter radius of circle:"))
print("1.Calculate Area")
print("2.Calculate Perimeter")
choice=int(input("enter 1 or 2 "))
if choice==1:
    print("Area of circle is:",3.14*radius**2)
else:
    print("Perimeter of circle is:",2*3.14*radius)