from heapq import heappush, heappop
def dijkstra(s, n): # (始点, ノード数)
    dist = [float('inf')] * n
    hq = [(0, s)] # (距離, ノード)
    dist[s] = 0
    while hq:
        p = heappop(hq)[1] # ノードを pop する
        for to, cost in cnt[p]: # ノード p に隣接しているノードに対して
            if dist[p] + cost < dist[to]: # = はつけない！！
                dist[to] = dist[p] + cost
                heappush(hq, (dist[to], to)) # 距離が小さい順にやっていくので距離を先に入れる
    return dist

v, e, r = map(int, input().split())
cnt = [[] for _ in range(v)]
for i in range(e):
    s, t, d = map(int, input().split())
    cnt[s].append((t, d))
di = dijkstra(r, v)
# print(di)
for i in di:
    if i == float('inf'):
        print('INF')
    else:
        print(i)