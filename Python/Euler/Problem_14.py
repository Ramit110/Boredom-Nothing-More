Mathses = __import__("Euler_Lib")

def Chal14(limit):#finds the largest colatz solution up to 'limit'
    long = [0, 0]
    for x in range(1, limit+1):
        length = 0; temp = x
        while (temp>1):
            if ((temp%2) == 1):
                temp=(temp*3)+1
            else:
                temp/=2
            length+=1
        if (length > long[0]):
            long[0] = length
            long[1] = x
    return long[1]


print(Chal14(1000000))
