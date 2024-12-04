#!/usr/bin/env python3

from typing import List

def read_lines(text: str) -> List[str]:
  return text.split('\n')

def read_file(path: str):
  with open(path, 'r') as file:
    return read_lines(file.read())

def get_matrix_from_file(path: str):
  return list(map(list,read_file(path)))

def is_mas_cross(m: List[List[str]], x: int, y: int) -> int:
  if not((0 < x < len(m[0])-1) and (0 < y < len(m)-1)):
    return 0
  comb = ["MS","SM"]
  if (m[y-1][x-1] + m[y+1][x+1] in comb) and (m[y-1][x+1] + m[y+1][x-1] in comb):
    return 1
  return 0

def search_xmas_count(matrix: List[List[str]]) -> int:
  count = 0
  for y,row in enumerate(matrix):
    for x,value in enumerate(row):
      if value == 'A':
        count += is_mas_cross(matrix,x,y)
  return count


def main():
  matrix = get_matrix_from_file('2024/day-4/data.txt')
  print(search_xmas_count(matrix))

if __name__ == "__main__":
    main()    


