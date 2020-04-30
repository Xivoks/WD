import numpy as np

fibonacci = []
midfibonacci = []
a = 1
b = 1
for x in range(5):
    for y in range(5):
        temp = b
        b += a
        a = temp
        midfibonacci.append(a)
    fibonacci.append(midfibonacci)
    midfibonacci = []
result = np.array(fibonacci)
print(result)
