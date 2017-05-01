Mathses = __import__("Euler_Lib")

def Chal12(limit):# finds the first triangular number with 'limit' factors
    x = 1
    while(True):
        temp = 0
        for y in range(1, x+1):
            temp+=y
        Arr = Mathses.Factorify(temp)
        if(len(Arr) >= limit):
            return temp
        x+=1

print(Chal12(500))
