def lista(**zakupy):
    ile = 0
    for i in zakupy:
        ile += zakupy[i]
    print("\nIlosc produktow łącznie:", ile)


lista(pomidor=2, olej=1, jablka=5, banany=2)
