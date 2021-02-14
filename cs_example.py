n, k = map(int, input().split())
a = list(map(int, input().split()))
num = sum(a[:k])
ans = num
for i in range(n-k):
    num += a[i+k] - a[i]
    ans += num
print(ans)