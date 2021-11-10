def dfs(node, computers, visited):
    visited[node] = True
    for i, v in enumerate(computers[node]):
        if v and i != node and not visited[i]:
            dfs(i, computers, visited)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for node in range(n):
        if not visited[node]:
            dfs(node, computers, visited)
            answer += 1
    
    return answer

if __name__ == '__main__':
    solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])