def AddBinary(Num1, Num2):
    c, Num1, Num2, out = 0, Num1[::-1], Num2[::-1], ""
    for x in range(0, len(Num1)):
        out+=str((int(Num1[x]) + int(Num2[x]) + c) % 2 )
        if((int(Num1[x]) + int(Num2[x]) + c) >= 2):
            c = 1
        else:
            c = 0
    return "("+str(c)+") "+out[::-1]
