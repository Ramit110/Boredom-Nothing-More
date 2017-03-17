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

print(DecToBin(2048))
