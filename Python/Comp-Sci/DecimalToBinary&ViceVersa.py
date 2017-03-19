def DecToBin(Dec):
    TBR = ""
    while(Dec>0):
        if((Dec%2) == 0):
            TBR+="0"
        else:
            TBR+="1"
        Dec = int(Dec/2)
    TBR = TBR[::-1]
    return TBR

def BinToDec(Bin):
    TBR = 0
    for x in range (0,len(Bin)):
        TBR+=int(int(Bin[x])*int((2**(len(Bin)-x-1))))
    return TBR

print(DecToBin(65))
print(BinToDec("101"))
