N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
B_min = max(A)
remain = N - K

for i in range(K + 1):
    B_min = min(B_min, A[i + remain - 1] - A[i])

print(B_min)
