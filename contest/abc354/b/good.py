def main():
    N = int(input())
    sc = [input().split() for i in range(N)]
    sc.sort()
    s, c = zip(*sc)
    print(s[sum(map(int, c))%N])
main()