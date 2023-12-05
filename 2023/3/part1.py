def sum_part_numbers(schematic):
    rows = schematic.split('\n')
    grid = [list(row) for row in rows]
    #init 2d array all false
    nonconnected_grid = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    total = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j].isdigit():
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        nx, ny = i + dx, j + dy
                        

                        if 0 <= nx < len(grid) and \
                           0 <= ny < len(grid[i]) and \
                           not grid[nx][ny].isdigit() and \
                           not grid[nx][ny].isalpha() and \
                           grid[nx][ny] != '.':
                            total += int(grid[i][j])
                    else:
                        continue
                    break
    return total

with open('2023/3/test.txt') as f:
        schematic = f.read()

print(sum_part_numbers(schematic.strip()))