def main():
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    C = sorted(A + B)

    if N < 2:
        print("No")
        exit()
    else:
        for i in range(N + M - 1):
            for j in range(N - 1):
                if C[i] == A[j] and C[i + 1] == A[j + 1]:
                        print("Yes")
                        exit()
                

    print("No")


main()