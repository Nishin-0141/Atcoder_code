from itertools import product
n, x = map(int, input().split())
a = list(map(int, input().split()))
for i in product([0, 1], repeat=n - 1): # 0は-, 1は+
    cnt = a[0]
    char = str(a[0])
    for j in range(n - 1):
        if i[j] == 0:
            cnt -= a[j + 1]
            char += ' - ' + str(a[j + 1])
        else:
            cnt += a[j + 1]
            char += ' + ' + str(a[j + 1])
    if cnt == x:
        print(char + ' = ' + str(x))
        exit()
print('None')
