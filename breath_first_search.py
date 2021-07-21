from collections import deque

r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
grid = [input() for _ in range(r)]
dist = [[0] * c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if grid[i][j] == '#':
            dist[i][j] = -1
q = deque()
q.append([sy - 1, sx - 1]) # スタート地点の(y, x)座標
d = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 上下左右に動く時の変化量
while q:
    v = q.popleft() # 現在地
    for dy, dx in d:
        if not (0 <= v[0] + dy <= r - 1 and 0 <= v[1] + dx <= c - 1): continue # (y, x)が範囲外のとき
        if dist[v[0] + dy][v[1] + dx] != 0: continue # 移動先が壁、もしくは訪問済みなら行かない
        dist[v[0] + dy][v[1] + dx] = dist[v[0]][v[1]] + 1 # 何歩目か更新
        q.append([v[0] + dy, v[1] + dx]) # キューに新しく追加

print(dist[gy - 1][gx - 1])
