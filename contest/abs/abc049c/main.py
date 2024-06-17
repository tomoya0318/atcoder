def main():
    S = input()[::-1]
    targets = ["dream", "dreamer", "erase", "eraser"]
    targets = [target[::-1] for target in targets]

    while len(S) > 0:
        matched = False
        for target in targets:
            if S.startswith(target):
                S = S[len(target):]
                matched = True
                break
        if not matched:
            break
    if not S:
        print("YES")
    else:
        print("NO")

main()