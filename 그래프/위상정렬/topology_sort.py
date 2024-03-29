from collections import deque

v, e = map(int, input().split())

# 진입차수
indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    # 진입차수 1 증가
    indegree[b] += 1

def topolgy_sort():
    result = [] # 수행 결과 담을 리스틀
    q = deque() # 큐 기능 위한 deque 라이브러리

    # 처음 시작시 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0 :
            q.append(i)
    
    # 큐가 빌 때까지 반복.
    while q :
        now = q.popleft()
        result.append(now)

        # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in result:
        print(i, end= ' ')

topolgy_sort()
