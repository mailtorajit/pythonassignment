num = input("Enter number:")
print(num)
reverse_number = 0
length = len(num)-1
for i in range(len(num)):
	reverse_number = reverse_number*10+int(num[length-i])

print(reverse_number)