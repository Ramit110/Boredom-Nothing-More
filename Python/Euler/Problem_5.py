Mathses = __import__("Euler_Lib")

def Chal5(limit):# Finds the smallest multiple beteen 1 and 'limit'
    Factors, FinalMult, TBR = Mathses.Factorify(limit), {}, 1
    for x in range(0, len(Factors)-1):
        temp, num = Factors[x], 1
        while(Mathses.IfPrime(int(temp)) == False):
            temp = int(temp**0.5)
            num+=1
        FinalMult[temp] = int(num)
    for x in len(FinalMult.values():
        TBR*=(x[0]**x[1])
    return TBR

print(Chal5(10))
