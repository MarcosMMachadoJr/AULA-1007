X = []

for i in range(5):
    X.append(int(input()))

    if X[i] <= 0:
        X[i] = 1

    print("X[{}] = {}" .format(i, X[i]))