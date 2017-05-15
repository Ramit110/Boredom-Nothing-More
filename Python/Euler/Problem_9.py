Mathses = __import__("Euler_Lib")

def Chal9(limit):# finds numbers that add to 'limit' and are pythagorean
    for a in range(1,limit):
        for b in range(a,limit):
            if(Mathses.IfNormalRoot((a**2)+(b**2), 2)):
                c = int(((a**2)+(b**2))**0.5)
                if(((a+b+c == limit) & ((a**2) + (b**2) == (c**2)))):
                    return (a*b*c)
    return 0

print(Chal9(1000))
