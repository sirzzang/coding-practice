def dfs(node, computers, visited):
    visited[node] = True
    for i, v in enumerate(computers[node]):
        # 연결되어 있는 컴퓨터의 경우 다시 탐색
        if v and i != node and not visited[i]:
            dfs(i, computers, visited)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for node in range(n):
        if not visited[node]:
            dfs(node, computers, visited)
            # 탐색 마친 경우 네트워크 추가
            answer += 1
    
    return answer

if __name__ == '__main__':
    solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])