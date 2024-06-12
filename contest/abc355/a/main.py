def main():
    A, B = map(int, input().split())

    suspect = [i for i in range(1, 4)]
    
    # tmp = [*suspect]
    if A in suspect:
        suspect.remove(A)
    if B in suspect:
        suspect.remove(B)

    if len(suspect) < 2:
        print(*suspect)
    else:
        print(-1)
    

main()