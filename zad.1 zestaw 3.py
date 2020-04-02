A = [1/x for x in range(1, 11)]
B = [2**i for i in range(1, 11)]
C = [x for x in B if x % 4 == 0]
print(A)
print(B)
print(C)
