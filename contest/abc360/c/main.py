N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

max_list = [0 for _ in range(N)]
all_sum = 0
tmp = A[0]

for i in range(N):
    # print(W[i])
    all_sum += W[i]
    num = A[i]
    if W[i] > max_list[num - 1]:
        max_list[num - 1] = W[i]


    
print(all_sum - sum(max_list))




