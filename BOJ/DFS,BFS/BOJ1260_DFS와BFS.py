from collections import deque

def dfs(graph, node, visited, answer):
    # 방문한 노드 처리
    visited[node] = True
    answer.append(str(node))
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, answer)

def bfs(graph, node, visited, answer):
    # 방문한 노드 처리
    queue = deque([node])
    visited[node] = True
    while queue:
        curr = queue.popleft()
        answer.append(str(curr))
        for neighbor in graph[curr]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
    return answer

n, m, v = map(int, input().split())
# graph = [[]]*n 

# graph 만들기
graph = [[] for _ in range(n+1)]
for _ in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

# 정점 번호 작은 순으로 그래프 정렬
graph = [sorted(x) for x in graph]

# dfs, bfs 수행
dfs_visited, bfs_visited = [False] * (n+1), [False] * (n+1)
dfs_answer, bfs_answer = [], []
dfs(graph, v, dfs_visited, dfs_answer)
print(' '.join(dfs_answer))
print(' '.join(bfs(graph, v, bfs_visited, bfs_answer)))