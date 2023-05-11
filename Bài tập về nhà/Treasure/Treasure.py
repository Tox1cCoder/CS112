from collections import deque

INF = int(1e9 + 7)
maze = [[0] * 14 for _ in range(14)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


class Node:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val


def valid(x, y):
    if x < 0 or x >= n or y >= n or y < 0 or maze[x][y] == -2:
        return False
    return True


def solve(cnt):
    q = deque()
    dp = [[[INF] * 14 for _ in range(15)] for _ in range(1 << 14)]
    dp[0][0][0] = 0
    q.append(Node(0, 0, 0))
    while len(q) > 0:
        curr = q.popleft()
        x, y, val = curr.x, curr.y, curr.val
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            newval = curr.val
            if not valid(nx, ny):
                continue
            if maze[nx][ny] >= 0:
                newval |= 1 << maze[nx][ny]
            if dp[newval][nx][ny] > dp[val][x][y] + 1:
                dp[newval][nx][ny] = dp[val][x][y] + 1
                if nx == n - 1 and ny == n - 1 and newval == ((1 << cnt) - 1):
                    return dp[(1 << cnt) - 1][nx][ny]
                ns = Node(nx, ny, newval)
                q.append(ns)

    return -1


n = int(input())
cnt = 0
arr = [list(input().strip()) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == '.':
            maze[i][j] = -1
        elif arr[i][j] == '#':
            maze[i][j] = -2
        else:
            maze[i][j] = cnt
            cnt += 1

print(solve(cnt))
