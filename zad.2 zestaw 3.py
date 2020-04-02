Matrix = [[a for a in range(1+4*b, 5+4*b)] for b in range(4)]
print(Matrix)
diagonal = [Matrix[x][x]for x in range(4)]
print(diagonal)
