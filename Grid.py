from sys import stdin

def bfs(grid, n, m):
    visited = []
    cue = []

    for i in range(n * m):
        visited.append(False)

    visited[0] = True
    coord = [0, 0, 0]
    cue.append(coord)

    while not len(cue) == 0:
        curr = cue.pop(0)
        row = int(curr[0])
        col = int(curr[1])
        moves = int(curr[2])

        if (row == n - 1) and (col == m - 1):
            return moves

        jump = grid[row + (col * n)]

        # Up
        up = row - jump
        up_coord = up + (col * n)
        if (up >= 0) and (not visited[up_coord]):
            cue.append([up, col, moves + 1])
            visited[up_coord] = True

        # Down
        down = row + jump
        down_coord = down + (col * n)
        if (down < n) and (not visited[down_coord]):
            cue.append([down, col, moves + 1])
            visited[down_coord] = True

        # Left
        left = col - jump
        left_coord = row + (left * n)
        if (left >= 0) and (not visited[left_coord]):
            cue.append([row, left, moves + 1])
            visited[left_coord] = True

        # Right
        right = col + jump
        right_coord = row + (right * n)
        if (right < m) and (not visited[right_coord]):
            cue.append([row, right, moves + 1])
            visited[right_coord] = True

    return -1


dem = list(stdin.readline().split())

y = int(dem[0])
x = int(dem[1])

grd = []

for i in range(y):
    rw = stdin.readline().strip()
    for j in range(x):
        grd.append(int(rw[j]))

print(bfs(grd, x, y))
