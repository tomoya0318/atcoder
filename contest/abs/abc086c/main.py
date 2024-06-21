def main():
    N = int(input())
    T, X, Y = [], [], []
    t_old = x_old = y_old = 0

    for _ in range(N):
        ti, xi, yi = map(int, input().split())
        T.append(ti)
        X.append(xi)
        Y.append(yi)

    for t, x, y in zip(T, X, Y):
        abel = abs(t_old - t)
        dist = abs(x_old - x) + abs(y_old - y)
        if (t + x + y) % 2 != 0 or abel < dist:
            print("No")
            exit()
            
        t_old = t
        x_old = x
        y_old = y
    
    print("Yes")

main()