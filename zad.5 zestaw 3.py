def sprawdz(a1, a2):
    if(a1 == a2):
        print("proste są równoległe")
    elif(a1*a2 == -1):
        print("proste są prostopadłe")
    else:
        print("proste nie są równoległe ani prostopadłe względem siebie")


test = sprawdz
test(1, 5)
