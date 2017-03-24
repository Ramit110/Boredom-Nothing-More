AddBin = __import__("0003_AddBinary")

def TwosComplement(Num):
    out = ""
    for x in range(0, len(Num)):
        if(Num[x] == "0"):
            out += "1"
        elif(Num[x] == "1"):
            out += "0"
    out = AddBin.AddBinary(out, ((len(out)-1)*"0")+"1")
    return out

print(TwosComplement(input("Enter Binary: ")))
