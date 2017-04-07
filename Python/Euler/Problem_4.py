Mathses = __import__("Euler_Lib")

def Chal4(limit):# Finds the largest two multiples that can be made up to 'limit'
    for x in range(1, limit):
        if(Mathses.IfPalindome((limit-x)*(limit)) == True):
            return limit-x



print(Chal4(99))
