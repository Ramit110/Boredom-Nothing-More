Mathses = __import__("Euler_Lib")

def Chal5(limit):# Finds the smallest multiple beteen 1 and 'limit'
    TBR = 1
    for x in range(2, limit):
        if(Mathses.IfPrime(x) == True):
            power = 1
            while((x**(power+1)) <= limit):
                power+=1
            TBR*=(x**power)
    return TBR

print(Chal5(20))
