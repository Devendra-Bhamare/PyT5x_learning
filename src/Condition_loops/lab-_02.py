

num1 = int(input("enter first no\n"))
num2 = int(input("enter second no\n"))
num3 = int(input("enter third no\n"))

if num1 > num2 and num1 > num3:
    print ("Max no is ", num1)
elif num2 >num1 and num2 > num3:
    print ("Max no is" ,num2)
else:
    print("Max no is ", num3)
