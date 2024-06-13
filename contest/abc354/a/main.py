def main():
    H = int(input())
    height = 0
    day = 0
    while True:
        if height > H:
            print(day)
            exit()
        else:
            height += 2 ** day
            day += 1

main()