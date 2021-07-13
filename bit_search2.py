n = int(input())
a = list(map(int, input().split()))

for i in range(2**n):
    cnt = ''
    for j in range(n):
        if (i >> j) & 1:
            cnt += str(a[j])
    print(cnt)
