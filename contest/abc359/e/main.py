N = int(input())
H = list(map(int, input().split()))

stack = [(H[0], 0)]
ans = []
t = 0

for i, h_i in enumerate(H, 1):
    height = 1
# for i, h_i in enumerate(h, 1):
#     height = 0
#     while stack and stack[-1][0] <= h_i:
#         x, j = stack.pop()
#         print(x, j)
#         t += (x - height) * (i - j)
#         height = x
#     t += (h_i - height) * (i - stack[-1][1]) + 1
#     stack.append([h_i, i])
#     ans.append(t)

# print(*ans)
# stack = [[float("inf"), 0]]
# if stack[-1][0] < H[1]:
#     print("in")
