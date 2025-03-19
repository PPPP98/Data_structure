def make_set(n):
    # 0부터 n-1까지 각 원소가 독립적인 집합을 형성하도록 초기화
    parent = [i for i in range(n)]
    rank = [0] * n
    return parent, rank

def find(x, parent):
    # 경로 압축을 적용한 find 함수
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(x, y, parent, rank):
    rootX = find(x, parent)
    rootY = find(y, parent)
    if rootX == rootY:
        return  # 이미 같은 집합에 속함
    # 랭크 기반 합치기
    if rank[rootX] < rank[rootY]:
        parent[rootX] = rootY
    elif rank[rootX] > rank[rootY]:
        parent[rootY] = rootX
    else:
        parent[rootY] = rootX
        rank[rootX] += 1