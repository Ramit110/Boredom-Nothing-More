Mathses = __import__("Euler_Lib")

def Chal7(limit):# returnsthe 'limit'th prime
    done, MATH, curr = True, [], 2
    while(done):
        if(Mathses.IfPrime(curr) == True):
            MATH.append(curr)
        if(len(MATH) >= limit):
            done = False
        curr+=1
    return MATH[limit-1]

print(Chal7(10001))
