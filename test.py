n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

if (n1>0 and n2>0) or (n1<0 and n2<0):
    print("Product is positive")
elif (n1>0 and n2<0) or (n1<0 and  n2>0):
    print("Product is negative")
else:
    print("Product is zero")