# 파이썬에서 queue를 구한할 때, list를 이용하면 pop시 모든 원소를 재배열해야해서 시간복잡도가 O(k)이다.
# 따라서 deque를 이용하여 queue를 이용하는 것이 좋음.

# 재귀함수란 자기 자신을 다시 호출하는 함수 (recusive function)
''' 무한히 함수 호출 but 파이썬은 최대 재귀 깊이가 정해져 있음.
def recursive_function():
    print('재귀함수를 호출합니다.')
    recursive_function()

recursive_function()'''

# 일반적으로 재귀함수의 종료 조건을 반드시 명시해야한다.
'''def recursive_function(i):
    if i == 100:
        return
    print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀함수를 종료합니다.')

recursive_function(1)'''

# 팩토리얼 구현
'''
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)'''

# 최대공약수 계산 (유클리드 호제법)

'''def ucld_reculsive(A,B):
    if A%B == 0:
        return B
    return ucld_reculsive(B, A%B)

print(ucld_reculsive(192,162))'''

# cf) 재귀함수, 반복문 동일한 기능을 수행할 수 있음.
# 유불리 따져서 선택할 것
# 스택을 사용해야 할 때 스택 라이브러리 대신에 재귀함수를 이용하는 경우가 많다.

#######################################################3
# DFS는 깊이 우선 탐색으로, 그래프의 깊은 부분을 우선적으로 탐색하는 알고리즘
# DFS는 스택 자료구조(혹은 재귀함수)를 이용한다.
# 1. 탐색 시작 노드를 스택에 삽입하고 방문처리
# 2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리한다.
#    방문하지 않은 인접노드가 없으면 스택에서 최상단 노드를 꺼낸다.
# 3. 더 이상 2번의 과정을 수행할 수 없을 때 까지 반복한다.

# DFS 메서드 정의
'''def dfs(graph, v, visited):
    #현재 노드를 방문처리
    visited[v] = True
    print(v, end = ' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph =[
    [], # 그래프가 대개 1부터 시작하므로 인덱스 0은 비워준다.
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트), False로 초기화
visited = [False] * 9

dfs(graph, 1 ,visited)'''

######################################################
# BFS
# 너비 우선 탐색으로 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘
# BFS는 큐 자료구조를 이용한다.
# 1. 탐색 시작 노드를 큐에 삽입하고 방문처리한다.
# 2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리한다.
# 3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.
'''
from collections import deque

#BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때 까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end=' ')
        #아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph =[
    [], # 그래프가 대개 1부터 시작하므로 인덱스 0은 비워준다.
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

#각 노드가 방문된 정보를 표현
visited = [False] * 9

#정의된 BFS 함수 호출
bfs(graph, 1, visited)'''

###############################################################################

#DFS & BFS 기초 문제 풀이

#음료수 얼려먹기

'''N, M = map(int, input().split())
ice = []
for i in range(N):
    ice.append(list(map(int, input())))
print(ice)

def dfs(x,y):
    #주어진 범위를 벗어나는 경우
    if x <= -1 or x>= N or y<=-1 or y >= M:
        return False
    #현재노드를 아직 방문하지 않았다면,
    if ice[x][y] == 0:
        #해당 노드방문 처리
        ice[x][y] = True
        #상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True

result = 0
for i in range(N):
    for j in range(M):
        #현재 위치에서 DFS 수행
        if dfs(i,j) == True:
            result += 1
            
'''

# 미로탈출 BFS
from collections import deque

n,m = map(int, input().split())
route = []
for i in range(n):
    route.append(list(map(int, input())))
print(route)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y= queue.popleft()
        continue
        if route[nx][ny] == 1:
            route[nx][ny] = route[x][y] + 1
            queue.append((nx, ny))
    return route[n - 1][m - 1]

print(bfs(0, 0))
for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if route[nx][ny] == 0:
                continue