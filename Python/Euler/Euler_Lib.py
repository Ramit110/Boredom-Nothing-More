def Factorify(Num1):
    Factors = []
    a = Factors.append
    for x in range(1, int(Num1**0.5)+1):
        if ((Num1%x)==0):
            a(int(x))
            a(int(Num1/x))
    return Factors

def Pascalify(Num1):
    TBR = [[1]]
    a = TBR.append
    for x in range(1, Num1):
        temp = []
        p = temp.append
        p(1)
        for y in range(1,x):
            p(TBR[x-1][y-1]+TBR[x-1][y])
        p(1)
        a(temp)
    return TBR

def IfNormalRoot(Num1, Power):
    Count=0
    while(str(Num1**(1/Power))[Count] != "."):
        Count+=1
    return ((Count+2)>=len(str(Num1**(1/Power))) & (str(Num1**(1/Power))[Count+1] == "0"))

def IfPrime(Num1):
    return len(Factorify(Num1)) == 2

def IfPalindome(Num1):
    return str(Num1) == str(Num1)[::-1]

