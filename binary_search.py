import math
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = []

for i in range(m):
    left = 0
    right = n - 1
    cnt = 0
    jud = 0
    while left <= right:
        mid = (left + right) // 2
        if a[mid] > b[i]:
            right = mid - 1
        elif a[mid] < b[i]:
            left = mid + 1
        else:
            print(mid + 1, end=' ')
            jud = 1
            break
    if jud == 0:
        print(-1, end=' ')