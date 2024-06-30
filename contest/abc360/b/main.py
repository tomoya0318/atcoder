S, T = input().split()

s_len = len(S)
t_len = len(T)

for w in range(1, s_len):
    for c in range(w):
        now = ""
        for i in range(c, s_len, w):
            now += S[i]
        
        if now == T:
            print("Yes")
            exit()

print("No")