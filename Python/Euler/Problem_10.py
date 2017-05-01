Mathses = __import__("Euler_Lib")

def Chal10(limit):# adds all the primes until 'limit'
    Out = 0
    for x in range(2, limit+1):
        if(Mathses.IfPrime(x) == True):
            Out+=x
    return Out

print(Chal10(2000000))
