def Chal3(limit): #Find The Largest Prime Factor Of 'limit'
	Factors = [1]
	TempFactor = [1]
	PFactor = 1
	for x in range(1,limit+1):
		if((limit%x)==0):
			Factors.append(x)

	for y in range(0,len(Factors)):
		for z in range(1,Factors[y]):
			if(((Factors[y]%z)==0) & (z!=1)):
				TempFactor.append(z)
			if(len(TempFactor)==2):
				PFactor = TempFactor[1]
				TempFactor = [1]
		
	return PFactor

# print(Chal3(600851475143))
print(Chal3(29))
