n, w = map(int, input().split())
num = [0]*(2*10**5 + 1)
for i in range(n):
    s, t, p = map(int, input().split())
    num[s] += p
    num[t] -= p
for i in range(2*10**5):
    num[i + 1] += num[i]
for i in range(2*10**5):
    if num[i] > w:
        print('No')
        exit()
print('Yes')
