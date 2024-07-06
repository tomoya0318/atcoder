C1 = list(map(int, input().split()))
C2 = list(map(int, input().split()))

x_c1 = abs(C1[0] - C1[3])
y_c1 = abs(C1[1] - C1[4])
z_c1 = abs(C1[2] - C1[5])

x_c2 = abs(C2[0] - C2[3])
y_c2 = abs(C2[1] - C2[4])
z_c2 = abs(C2[2] - C2[5])

if C1[0] < C2[0] < C1[3] or C2[0] < C1[0] < C2[3]:
    if C1[1] < C2[1] < C1[4] or C2[1] < C1[1] < C2[4]:
        if C1[2] < C2[2] < C1[5] or C2[2] < C1[2] < C2[5]:
            print("Yes")
            exit()
print("No")