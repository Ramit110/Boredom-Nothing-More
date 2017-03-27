def Chal1(limit): #Add All Multiples Of 3 And 5 UIntil 'limit'
	TBR = []
	for x in range(1,limit):
		if(((x%3)==0) | ((x%5)==0)):
			TBR.append(x)
	return sum(TBR)

print(Chal1(1000))

