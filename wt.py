L = [[i] for i in range(10)]
L = list(filter(lambda obj: obj[0] < -5, L))

print(L)