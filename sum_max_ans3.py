list_num = [3,6, 7,34,56,87,34,12, 199]
list_sum=0
list_max=0
for i in range(len(list_num)):
	list_sum=list_sum+list_num[i]
	if(list_num[i] > list_max):
		list_max = list_num[i]
		
print("Sum is "+ str(list_sum))
print("Max num is "+str(list_max))