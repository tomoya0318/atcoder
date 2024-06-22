def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = 0
    tmp = 0

    for i in range(len(A) - 2):
        tmp = A[i]
        if tmp == A[i + 2] and tmp != A[i + 1]: 
            count += 1

    print(count)
main()