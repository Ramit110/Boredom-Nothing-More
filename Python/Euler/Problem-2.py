def Chal2(limit): #Add All Even Fibionacci Numbers Until 'limit'
	TBR, Sequences = 0, [1,2]
	while(max(Sequences) < limit):
		Sequences.append(Sequences[len(Sequences)-1] + Sequences[len(Sequences)-2])

	for x in range(0,len(Sequences)-1):
		if((Sequences[x]%2)==0):
			TBR+=Sequences[x]	
	return TBR

print(Chal2(4000000))
