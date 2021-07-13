from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n)] # graph[i][j] := ノードiと隣接しているノードj
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
print(graph)
q = deque()
q.append([0]) # 初期ノードを挿入
dist = [-1]*n # dist[i] := ノードiに行くための最短距離
while q:
    v = q.popleft() # 現在地を取得
    for i in graph[v]: # 訪問先を探索
        if dist[i] != -1: continue # すでに行っているノードなら行かない
        dist[i] = dist[v] + 1 # 前のノードからコストを1増やす
print(dist)