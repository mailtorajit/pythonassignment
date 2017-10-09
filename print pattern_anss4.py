for i in range(0, 11):
	for j in range(0, 11):
		if (i==0 or i==5 or i==10) and (j==0 or j ==5 or j==10):
			print("+", end="")
		else:
			if(i==0 or i==5 or i==10) and (j!=0 or j !=5 or j!=10):
				print("-", end="")
			elif(i!=0 or i!=5 or i!=10) and (j==0 or j ==5 or j==10):
				print("|", end="")
			else :
				print(" ", end="")
	print(end="\n")

