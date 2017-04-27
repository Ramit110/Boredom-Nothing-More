Mathses = __import__("Euler_Lib")

def Chal6(limit):# returns the difference of the sum and squares of all natural numbers until 'limit'
    sqr, tot = 0, 0
    for x in range(1, limit+1):
        sqr+=int(Mathses.Powerify(x, 2))
        tot+=int(x)
    tot=int(Mathses.Powerify(tot, 2))
    return(int(tot)-int(sqr))

print(Chal6(100))
