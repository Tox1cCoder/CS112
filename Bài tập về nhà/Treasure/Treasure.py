import heapq

memo = {(i, 0): 0 for i in range(1 << 5)}
size = int(input())
board = [list(input()) for _ in range(size)]
e = []

def dp(mask, curr_treasure):
    if (mask, curr_treasure) in memo:
        return memo[(mask, curr_treasure)]
        
    if mask == (1 << len(e)) - 1:
        return abs(size - 1 - curr_treasure[0]) + abs(size - 1 - curr_treasure[1])
        
    min_distance = float('inf')
    
    for i, treasure in enumerate(e):
        if mask & (1 << i) == 0:
            next_distance = abs(treasure[0] - curr_treasure[0]) + abs(treasure[1] - curr_treasure[1])
            new_mask = mask | (1 << i)
            subproblem = dp(new_mask, treasure)
            min_distance = min(min_distance, next_distance + subproblem)

    memo[(mask, curr_treasure)] = min_distance
    return min_distance

def find_shortest_path(start, end, treasures):
    pq = [(0, start, set())]
    visited = set()
    while pq:
        cost, current, collected = heapq.heappop(pq)
        
        if current == end and len(collected) == len(treasures):
            return cost
            
        if (current, tuple(collected)) in visited:
            continue
            
        visited.add((current, tuple(collected)))
        i, j = current
        
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= x < size and 0 <= y < size and board[x][y] != '#':
                new_collected = collected.copy()
                if board[x][y] == '*':
                    new_collected.add((x, y))
                new_cost = cost + 1
                new_state = (new_cost, (x, y), new_collected)
                if (x, y, tuple(new_collected)) not in visited:
                    heapq.heappush(pq, new_state)
    return -1

start = (0, 0)
end = (size-1, size-1)
q = [(i, j) for i in range(size) for j in range(size) if board[i][j] == '*']
print(find_shortest_path(start, end, set(q)))
