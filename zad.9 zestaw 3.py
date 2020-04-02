def ciag(* liczby):
    if len(liczby) == 0:
        return 0.0
    else:
        suma = 1
        for i in liczby:
            suma *= i
        return suma


print(ciag(1, 2, 3, 4, 5, 6, 7, 8))
