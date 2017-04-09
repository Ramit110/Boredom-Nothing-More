# ???

Mathses = __import__("Euler_Lib")

'''
def Chal5(limit):# Finds the smallest multiple beteen 1 and 'limit'
    Factors, FinalMult, TBR = Mathses.Factorify(limit), {}, 1
    for x in range(1, limit):
        if(Mathses.IfPrime(x) == True):
            FinalMult[x] = 1
        elif(Mathses.IfNormalRoot(x) == True):
            temp = x
            temp=int(temp**0.5)
            while(Mathses.IfNormalRoot(temp) == True):
                temp=int(temp**0.5)
            FinalMult[temp] = FinalMult[temp]+1
    for k, v in FinalMult.items():
        TBR*=int(Mathses.Powerify(k, v))
    return TBR
'''

def Chal5(limit):
    Factors = Mathes.Fectorify(limit)
    return Num1

print(Chal5(10))
