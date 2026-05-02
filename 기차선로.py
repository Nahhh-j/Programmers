'''
문제 설명
n × m 크기의 직사각형 격자가 있습니다. 격자의 가장 왼쪽 위는 (1, 1), 가장 오른쪽 아래는 (n, m)입니다. 각 격자칸은 빈칸, 선로, 장애물 중 하나입니다. 선로는 7가지 종류가 있으며 아래 그림과 같습니다.
ex1-1.png
격자의 (1, 1)에는 1번 선로가 놓여있고, (n, m)에는 1번, 2번 선로 중 하나가 놓여있습니다. 당신은 기차가 (n, m)에 도착할 수 있도록 격자의 빈칸에 선로를 놓으려 합니다. (선로를 놓지 않고 빈칸인 채로 두어도 됩니다.) 당신이 선로를 완성시키면 기차가 (1, 1)에서 오른쪽 방향으로 출발해 선로를 따라 움직입니다. 이때 기차는 격자에 있는 모든 선로를 한번 이상 지나가야 합니다. 또한, # 모양의 3번 선로는 상하좌우 모든 방향으로 연결되어 있어야 합니다.
당신은 격자의 정보가 주어질 때 격자에 선로를 놓는 방법의 수를 알고 싶습니다.
아래는 n = 3, m = 3인 격자의 예시입니다.
ex1-2.png
이 격자에 선로를 놓는 방법은 아래 2가지입니다.
ex1-3.png
격자의 정보를 담고 있는 2차원 정수 배열 grid가 매개변수로 주어집니다. 이때, 격자에 선로를 놓는 방법의 수를 return 하도록 solution 함수를 완성해 주세요. 어떻게 선로를 놓아도 문제의 조건을 만족시킬 수 없다면 0을 return 합니다.

제한사항
2 ≤ grid의 세로 길이 = n ≤ 8
2 ≤ grid의 가로 길이 = m ≤ 8
grid[i][j]는 (i+1, j+1) 위치의 격자칸 정보를 나타냅니다. 격자칸이 빈칸인 경우 0, 선로인 경우 각 선로의 번호(1 ~ 7), 장애물인 경우 -1입니다.
grid[0][0] = 1
grid[n-1][m-1] = 1 or 2
grid에서 빈칸이 한 번 이상 등장합니다.
n × m ≤ 20
'''

def solution(grid):
    n, m = len(grid), len(grid[0])
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    rail = {
        1: {1:1, 3:3},
        2: {0:0, 2:2},
        3: {0:1, 1:0, 2:3, 3:2},
        4: {2:1, 3:0},
        5: {0:1, 3:2},
        6: {0:3, 1:2},
        7: {1:0, 2:3},
    }
    
    total = n * m
    answer = 0
    
    visited = [[False]*m for _ in range(n)]
    
    def dfs(x, y, d, cnt):
        nonlocal answer
        
        # 범위 밖 or 장애물
        if not (0 <= x < n and 0 <= y < m):
            return
        if grid[x][y] == -1:
            return
        
        # 도착
        if (x, y) == (n-1, m-1):
            if cnt == total:
                answer += 1
            return
        
        # 이미 방문한 경우
        if visited[x][y]:
            return
        
        visited[x][y] = True
        
        # 현재 칸
        if grid[x][y] != 0:
            t = grid[x][y]
            if d not in rail[t]:
                visited[x][y] = False
                return
            
            nd = rail[t][d]
            nx = x + dx[nd]
            ny = y + dy[nd]
            dfs(nx, ny, nd, cnt+1)
        
        else:
            # 빈칸 → 모든 선로 시도
            for t in range(1, 8):
                if d not in rail[t]:
                    continue
                
                nd = rail[t][d]
                
                # 3번은 4방향 연결 필요 → 나중에 체크
                grid[x][y] = t
                
                nx = x + dx[nd]
                ny = y + dy[nd]
                dfs(nx, ny, nd, cnt+1)
                
                grid[x][y] = 0
        
        visited[x][y] = False
    
    # 시작 (0,0)에서 오른쪽 방향(1)
    dfs(0, 0, 1, 1)
    
    return answer