Mathses = __import__("Euler_Lib")

def Chal8(limit):# finds all
    for a in range(1,limit):
        for b in range(a,limit):
            for c in range(b,limit):
                if((a+b+c) == limit) & ((Mathses.Powerify(a,2) + Mathses.Powerify(b,2) == Mathses.Powerify(c,2))):
                   return (a*b*c)
    return 0

print(Chal8(1000))
