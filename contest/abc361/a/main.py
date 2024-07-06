N, M, K = map(int, input().split())
A = list(map(int, input().split()))

Afront, Aback = A[:M], A[M:]
Afront.append(K)
print(*(Afront + Aback))