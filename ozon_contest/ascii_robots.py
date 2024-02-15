from io import StringIO
import sys
from ozon_contest.test_utils import prepare_input, compare_outputs
from time import time

def find_route(grid, start, end):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # up and down, right and left
    queue = [start]
    visited = set()
    paths = {start: []}

    while queue:
        x, y = queue.pop(0)
        if (x, y) == end:
            return paths[end]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '.' and (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.add((nx, ny))
                paths[(nx, ny)] = paths[(x, y)] + [(nx, ny)]

    return None
def fast_input():
    return sys.stdin.readline().rstrip("\r\n")

def fast_output(x):
    sys.stdout.write(str(x))

if __name__ == '__main__':
    input_files, output_files = prepare_input('./input/ascii_robots/*')
    begin = time()
    for idx_file in range(len(input_files)):
        # putting program output into buffer to compare with answer later
        output_buffer = StringIO()
        tmp = sys.stdout
        sys.stdout = output_buffer
        # MAIN LOGIC
        with open(input_files[idx_file], "r") as input_file:
            # if idx_file == 1: sys.exit(0)
            t = int(input_file.readline())
            for _ in range(t):
                n, m = map(int, input_file.readline().split())
                grid = [input_file.readline().rstrip() for _ in range(n)]
                start_A = (next((i, j) for i in range(n) for j in range(m) if grid[i][j] == 'A'))
                start_B = (next((i, j) for i in range(n) for j in range(m) if grid[i][j] == 'B'))
                if start_A[0] < start_B[0]:
                    route_A = find_route(grid, start_A, (0, 0))
                    route_B = find_route(grid, start_B, (n - 1, m - 1))
                elif start_A[0] > start_B[0]:
                    route_A = find_route(grid, start_A, (n - 1, m - 1))
                    route_B = find_route(grid, start_B, (0, 0))
                elif start_A[1] < start_B[1]:
                    route_A = find_route(grid, start_A, (0, 0))
                    route_B = find_route(grid, start_B, (n - 1, m - 1))
                else:
                    route_A = find_route(grid, start_A, (n - 1, m - 1))
                    route_B = find_route(grid, start_B, (0, 0))
                for i, j in route_A:
                    grid[i] = grid[i][:j] + 'a' + grid[i][j + 1:]
                for i, j in route_B:
                    grid[i] = grid[i][:j] + 'b' + grid[i][j + 1:]

                for row in grid:
                    print(row)
        # MAIN LOGIC END
        sys.stdout = tmp

        compare_outputs(output_files[idx_file], output_buffer)
    end = time()
    print(f'{end - begin} sec')
