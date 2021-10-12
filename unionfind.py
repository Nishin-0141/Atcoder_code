# この Union Find はランクなしの場合

# 木の根を求める
def root(x: int) -> int:
    if par[x] == x:             # 根
        return x
    else:
        par[x] = root(par[x])   # 経路圧縮
        return par[x]


# x と y が同じ集合に属するかどうか
def same(x: int, y: int) -> bool:
    return root(x) == root(y)


# x と y の属する集合を併合
def unite(x: int, y: int):
    x = root(x)
    y = root(y)
    if x == y: return
    par[x] = y


n, q = map(int, input().split())
par = [i for i in range(n)] # はじめは全部の頂点が根
for i in range(q):
    p, a, b = map(int, input().split())
    a -= 1
    b -= 1
    if p == 0:
        unite(a, b)
    else:
        if same(a, b):
            print('Yes')
        else:
            print('No')