from LinkedList.DobleLinkedList import Deque

def bfs(s):
    visited = [False] * (V + 1)
    que = Deque()
    que.append(s)
    visited[s] = True
    while que:
        v = que.pop()
        print(v, end=" ")
        for w in graph[v]:
            if not visited[w]:
                visited[w] = True
                que.append(w)


V = 7

graph = [
    [],
    [2, 3, 4],
    [1, 6],
    [1, 4, 5, 6],
    [1, 3, 5],
    [3, 4],
    [2, 3, 7],
    [6]
]

# for i in range(1, V + 1):
#     graph[i].sort(reverse = True)

bfs(1)