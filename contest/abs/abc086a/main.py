def main():
    a, b = map(int, input().split())
    ans = a * b

    if(ans % 2 == 1):
        print("Odd")
    else:
        print("Even")


main()