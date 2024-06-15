import sys
def main():
    line = sys.stdin.read().strip()
    N, *d = line.split("\n")

    print(len(set(d)))
main()