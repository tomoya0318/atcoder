def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    X = [list(map(int, input().split())) for _ in range(N)]

    for i in range(M):
        j_num = 0
        for j in range(N):
            j_num += X[j][i]
        if  j_num < A[i]:
            print("No")
            return

    print("Yes")
    
if __name__ == "__main__":
    main()