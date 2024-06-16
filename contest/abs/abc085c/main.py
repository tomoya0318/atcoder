def main():
    N, Y = map(int, input().split())

    T_TH = 10000
    F_TH = 5000
    O_TH = 1000

    x = y = z = 0

    for t in range(N + 1):
        x = t
        for f in range(N + 1):
            y = f
            z = N - x - y
            if z < 0:
                continue
            ans = x * T_TH + y * F_TH + z * O_TH
            if ans == Y:
                print(f"{x} {y} {z}")
                exit()

                            
    print(f"{-1} {-1} {-1}")
main()