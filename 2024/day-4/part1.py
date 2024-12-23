#!/usr/bin/env python3

from typing import List

def read_lines(text: str) -> List[str]:
  return text.split('\n')

def read_file(path: str):
  with open(path, 'r') as file:
    return read_lines(file.read())

def get_matrix_from_file(path: str):
  return list(map(list,read_file(path)))

def traverse(matrix: List[List[str]], x: int, y: int, dir: int, rest: List[str]) -> int:
  # Implement the traverse function logic
  dx = [0, 1, 1, 1, 0, -1, -1, -1]
  dy = [1, 1, 0, -1, -1, -1, 0, 1]
  for i, char in enumerate(rest):
    nx, ny = x + dx[dir] * (i + 1), y + dy[dir] * (i + 1)
    if not (0 <= nx < len(matrix[0]) and 0 <= ny < len(matrix)) or matrix[ny][nx] != char:
      return 0
  return 1

def search_xmas_count(matrix: List[List[str]]) -> int:
  count = 0
  for y,row in enumerate(matrix):
    for x,value in enumerate(row):
      if value == 'X':
        for dir in range(8):
          count += traverse(matrix,x,y,dir,['M','A','S'])
  return count


def main():
  matrix = get_matrix_from_file('2024/day-4/data.txt')
  print(search_xmas_count(matrix))

if __name__ == "__main__":
    main()    


