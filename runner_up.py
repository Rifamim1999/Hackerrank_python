if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    b = sorted(arr, reverse = True)
    for i in range(1, n):
        if b[0]>b[i]:
            print(b[i])
            break
