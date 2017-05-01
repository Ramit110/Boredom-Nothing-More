#def SqaureRootify(Num1):
#    TBR = 0
#    while (round(TBR)*(round(TBR)) <= Num1):
#        TBR+=0.1
#    return TBR

def Powerify(Num1, Power):
    TBR = Num1
    for x in range(1, Power):
        TBR*=Num1
    return TBR

def Factorify(Num1):
    Factors = []
    for x in range(1, int(Num1**0.5)+1):
        if ((Num1%x)==0):
            Factors.append(int(x))
            Factors.append(int(Num1/x))
    return Factors

def IfNormalRoot(Num1, Power):
    Count=0
    while(str(Num1**(1/Power))[Count] != "."):
        Count+=1
    if(((Count+2)>=len(str(Num1**(1/Power)))) & (str(Num1**(1/Power))[Count+1] == "0")):
        return True
    return False

def IfPrime(Num1):
    if (len(Factorify(Num1)) <= 2):
        return True
    return False

def IfPalindome(Num1):
    if(str(Num1) == str(Num1)[::-1]):
        return True
    return False
