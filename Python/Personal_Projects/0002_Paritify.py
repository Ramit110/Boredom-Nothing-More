def Paritify(Bits, Mode):
    Count = 0
    for x in range(0, len(Bits)):
        if (Bits[x] == "1"):
            Count+=1
    if (Mode == 0):#Odd parity
        return str(Count%2).replace("0", "1").replace("1", "0")+Bits
    elif (Mode == 1):#Even parity
        return str(Count%2)+Bits
    return "ERROR"


def CheckParity(Bits, Mode):
    Count = 0
    for x in range(0,len(Bits)):
        if (Bits[x] == "1"):
            Count+=1
    if (Mode == 0):#Odd Parity
        if((Count%2)==1):
            return True
        return False
    elif (Mode == 1):#Even parity
        if((Count%2)==0):
            return True
        return False
    return "ERROR"
