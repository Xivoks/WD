#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from totomodul import ustawienia, wyniki, losujliczby, pobierztypy


def main(args):
    # ustawienia gry
    nick, ileliczb, maksliczba, ilerazy = ustawienia()

    # losujemy liczby
    liczby = losujliczby(ileliczb, maksliczba)

    # pobieramy typy użytkownika i sprawdzamy, ile liczb trafił
    for i in range(ilerazy):
        typy = pobierztypy(ileliczb, maksliczba)
        iletraf = wyniki(set(liczby), typy)

    print("Wylosowane liczby:", liczby)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
