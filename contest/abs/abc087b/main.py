import sys
def main():
    input_data = sys.stdin.read().split()
    A, B, C, X = map(int, input_data)
    A, B, C = 500 * A, 100 * B, 50 * C
    count = 0

    for a in range(0, A + 1, 500):
        if a == X:
            count += 1
            continue
        for b in range(0, B + 1, 100):
            if a + b == X:
                count += 1
                continue
            for c in range(0, C + 1, 50):
                if a + b + c == X:
                    count += 1

    print(count)
main()