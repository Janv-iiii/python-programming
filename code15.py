#WAP to print whether a given character is an uppercase or a lowercase character or a digit or any other character
ch=input("enter any character:")
if(ch>='A' and ch<='Z'):
    print("You entered a uppercase letter")
elif(ch>='a' and ch<='z'):
    print("You entered a lowercase letter")
elif(ch>='0' and ch<='9'):
    print("You entered a digit")
else:
    print("You entered a special character")
