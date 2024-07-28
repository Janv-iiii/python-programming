#WAP that reads three numbers(integers)and print them in ascending order...
x=int(input("enter a no. x:"))
y=int(input("enter a no. y:"))
z=int(input("enter a no. z:"))
minn=mid=maxx=None
if(x<y and x<z):
    if(y<z):
        minn,mid,maxx=x,y,z
    else:
        minn,mid,maxx=x,z,y
if(y<x and y<z):
    if(x<z):
        minn,mid,maxx=y,x,z
    else:
        minn,mid,maxx=y,z,x
if(z<y and z<x):
    if(y<x):
        minn,mid,maxx=z,y,x
    else:
        minn,mid,maxx=z,x,y
print("Ascending order of these no.'s is:",minn,mid,maxx)        
    

    




