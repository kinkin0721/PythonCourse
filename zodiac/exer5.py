def findnumber():
    ahua = ""
    for n in range(2000, 3201):
       if n % 7 == 0 and n % 5 != 0:
           ahua = ahua + str(n) + ","
    print(ahua)

findnumber()
