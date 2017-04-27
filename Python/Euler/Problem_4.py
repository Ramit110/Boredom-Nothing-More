Mathses = __import__("Euler_Lib")

def Chal4(limit):# Finds the largest two multiples that can be made up to 'limit'
    for x in range(1, limit):
        if(Mathses.IfPalindome((limit-x)*(limit)) == True):
            return limit*(limit-x)
    return 0

out = 0
for x in range(999):
    if(Chal4(x) >= out):
        out=Chal4(x)
print(out)
