def taks(hoa,oppv,leeftijd):
    if hoa.upper() =="H" and leeftijd > 20 or hoa.upper() == "H" and oppv > 200 or hoa.upper() == "A" and leeftijd > 50:
        print("Extra betalen")
    else:
        print("Niet extra")



hoa = input("(H)uis of (A)ppartement")
oppv = int(input("Geef de oppervlakte"))
leeftijd = int(input("geef de leeftijd"))

#taks(hoa,oppv,leeftijd)

if hoa.upper() =="H" and leeftijd > 20:
    print("x")
elif hoa.upper() == "H" and oppv > 200:
    print("x")
elif hoa.upper() == "A" and leeftijd > 50:
    print("x")
else:
        print("Niet extra")




