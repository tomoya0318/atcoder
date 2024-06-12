def main():
    N, L, R = map(int, input().split(" "))
    A = []
    
    for i in range(1, L):
        A.append(i)
    
    for i in reversed(range(L, R + 1)):
        A.append(i)
    
    for i in range(R + 1, N + 1):
        A.append(i)

    for i, val in enumerate(A):
        if i == len(A) - 1:
            print(val)
        else:
            print(val, end=" ")

main()