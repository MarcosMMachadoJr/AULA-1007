A = []

for i in range(100):
    A.append(float(input()))

    if A[i] <= 10:
        print("A[{}] = {}" .format(i, A[i]))