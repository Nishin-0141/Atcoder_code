class UnionFind():
    def __init__(self, n: int) -> None:
        self.n = n
        self.par = [-1]*n

    def find(self, x: int) -> int:
        "要素が属する集合の代表を見つけて返す"
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def same(self, x: int, y: int) -> bool:
        "２つの根が同じかどうかを返す"
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> None:
        "２つの集合を１つに統合する"
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        else:
            if self.par[x] > self.par[y]:
                x, y = y, x
            self.par[x] += self.par[y]
            self.par[y] = x

    def size(self, x: int) -> int:
        "連結成分の大きさを返す"
        return -self.par[self.find(x)]

    def get_par(self):
        print(self.par)


n, q = map(int, input().split())
num = UnionFind(n)
for i in range(q):
    t, u, v = map(int, input().split())
    if t == 0:
        num.union(u, v)
    else:
        if num.same(u, v):
            print(1)
        else:
            print(0)
