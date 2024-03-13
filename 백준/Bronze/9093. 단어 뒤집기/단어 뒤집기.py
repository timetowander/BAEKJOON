for _ in range(int(input())):
    sen = list(input().split())
    for i in sen:
        print(i[::-1], end =" ")
    print()