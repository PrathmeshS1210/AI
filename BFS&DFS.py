# BFS DFS

n = int(input("Vertices: "))
e = int(input("Edges: "))
adj = [[] for _ in range(n)]

for _ in range(e):
    u, v = map(int, input().split())
    adj[u].append(v)

def bfs(s):
    vis = [False]*n
    q = [s]
    vis[s] = True
    while q:
        u = q.pop(0)
        print(u, end=' ')
        for v in adj[u]:
            if not vis[v]:
                q.append(v)
                vis[v] = True

def dfs(s):
    vis = [False]*n
    st = [s]
    vis[s] = True
    while st:
        u = st.pop()
        print(u, end=' ')
        for v in adj[u]:
            if not vis[v]:
                st.append(v)
                vis[v] = True

print("BFS:")
bfs(0)
print("\nDFS:")
dfs(0)
