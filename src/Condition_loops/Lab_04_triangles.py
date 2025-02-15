
side1 = int(input("Enter a first side"))
side2 = int(input("Enter a second side"))
side3 = int(input("Enter a third side"))

if side1 == side2 and side2 == side3:
    print("Equilteral triangle")
elif side1 == side2 or side2 == side3 or side1== side3:
    print ("isocles triangle")
else:
    print("scalene")