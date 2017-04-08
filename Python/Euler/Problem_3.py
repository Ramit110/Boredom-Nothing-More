def Chal3(limit): #Find The Largest Prime Factor Of 'limit' (if there is one)
    Factors, TempFactor, PFactor = [], [], 0
    for x in range(1,int(limit**0.5)+1):
        if((limit%x)==0):
            Factors.append(x)
            Factors.append(limit/x)
    for y in range(1,len(Factors)):
        for z in range(1,int(Factors[y]**0.5)+1):
            if((Factors[y]%z)==0):
                TempFactor.append(z)
                TempFactor.append(Factors[y]/z)
        if(len(TempFactor)==2):
            PFactor = TempFactor[1]
        TempFactor = []
    return int(PFactor)

# print(Chal3(600851475143))
print(Chal3(600851475143))
