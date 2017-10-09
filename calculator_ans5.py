operator = input("Enter operaraot in +-*/ :")
num1 = int(input("Enter input one:"))
num2 = int(input("Enter input two:"))


if operator == "+":
	print("Sum is : " + str(num1+num2))
elif operator == "-":
	print("Subtraction is : " + str(num1-num2))
elif operator == "*":
	print("multiplication is : " + str(num1*num2))
elif operator == "/":
	print("Divide is : " + str(num1/num2))
else :
	print("Entered wrong operator")	