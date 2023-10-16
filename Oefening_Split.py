
# -----------------------------------------------------------------------------------------------------------------------------------------
# Schrijf een functie split getallen, naar D H T E. bvb 1234
# 1D + 2H +3T+ 4E
# -----------------------------------------------------------------------------------------------------------------------------------------
def split():

    getal=(input("Geef een getal <100000: "))
    list1= list(getal)
    list1.reverse()
    list2 = ["E","T","H","D","TD"]
    list_comb=[]
    for i in range(0,len(list1)):
        list_comb.append(list1[i]+list2[i])
    list_comb.reverse()
    return list_comb

list1 = split()
for i in list1:
    print(i, end=" ")

