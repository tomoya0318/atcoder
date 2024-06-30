S = input()

list(S)
tmp = S[0]
for s in S:
    if tmp == "R":
        if s == "M":
            print("Yes")
            exit()
    else:
        tmp = s
print("No")
        