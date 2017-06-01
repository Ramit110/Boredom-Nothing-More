AddBin = __import__("0003_AddBinary")

def TwosComplement(Num):
    out = ""
    for x in range(0, len(Num)):
        if(Num[x] == "0"):
            out += "1"
        elSE:
            out += "0"
    return AddBin.AddBinary(out, ((len(out)-1)*"0")+"1")

print(TwosComplement(input("Enter Binary: ")))
