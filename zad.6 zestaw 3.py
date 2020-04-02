import math


def promien(x, y, a=0, b=0):
    r = ((x-a)**2)+((y-b)**2)
    dl = math.sqrt(r)
    print("promien =", dl)


dlugoscpromienia = promien
dlugoscpromienia(3, 5, 5, -2)
