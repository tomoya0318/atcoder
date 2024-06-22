def main():
    N = int(input())
    S = []
    count = 0
    for _ in range(N):
        S.append(input())

    for name in S:
        if name == "Takahashi":
            count += 1

    print(count)
main()