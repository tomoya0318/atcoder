def main():
    N = int(input())
    S = []
    C = []
    for _ in range(N):
        name, rate = input().split()
        S.append(name)
        C.append(int(rate))

    S = sorted(S)
    mod = sum(C) % N

    print(S[mod])


main()