from heapq import heappush, heappop
# Manhattan distance
def heuristic(a, b):
return abs(a[0] - b[0]) + abs(a[1] - b[1])
def astar(grid, start, goal):
open_list = []
heappush(open_list, (0, start, [start]))
visited = set()
while open_list:
_, current, path = heappop(open_list)
if current == goal:
return path
if current in visited:
continue
visited.add(current)
x, y = current
for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
nx, ny = x + dx, y + dy
if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
if grid[nx][ny] == 0 and (nx, ny) not in visited:
new_path = path + [(nx, ny)]
cost = len(new_path) + heuristic((nx, ny), goal)
heappush(open_list, (cost, (nx, ny), new_path))
return None # No path found
grid = [
[0, 0, 0, 0, 1],
[1, 1, 0, 1, 0],
[0, 0, 0, 0, 0],
[0, 1, 1, 1, 0],
[0, 0, 0, 0, 0]
]
start = (0, 0)
goal = (4, 3)
path = astar(grid, start, goal)
if path:
print("Path found:")
print(path)
else:
print("No path found.")
PROBLEMS OUTPUT DEBUG CONSOLE TERMINAL PORTS Filter
[Running] python -u "C:\Users\STUDEN~1.LAB\AppData\Local\Temp\tempCodeRunnerFile.python"
Path found:

[(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4)]
[Done] exited with code=0 in 0.089 seconds
No
[Running] python -u "C:\Users\STUDEN~1.LAB\AppData\Local\Temp\tempCodeRunnerFile.python"
path found.
[Done] exited with code=0 in 0.071 seconds
[Running] python -u "C:\Users\STUDEN~1.LAB\AppData\Local\Temp\tempCodeRunnerFile.python"
Path found:
[(8, 0), (8, 1), (0, 2), (1, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4), (4, 3)]
[Done] exited with code=0 in 0.091 seconds
