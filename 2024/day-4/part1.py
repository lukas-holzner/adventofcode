#!/usr/bin/env python3

def read_lines(text: str) -> list(str):
  return text.split('\n')

def read_file(path: str):
  with open(path, 'r') as file:
    return read_lines(file.read())

def get_matrix_from_file(path: str):
  return list(map(list,read_file(path)))

def traverse(matrix, x: int, y: int, dir: int, rest: list(str)):
  #TODO

def search_xmas_count(matrix: list(list(str))) -> int:
 count = 0
  for y,row in enumerate(matrix):
    for x,value in enumerate(row):
      if value == 'X':
        for dir in range(8):
          count = traverse(matrix,x,y,dir,['M','A','S'])
  return count


def main():
  matrix = get_matrix_from_file('day-4/data.txt')
  print(search_xmas_count(matrix))

if __name__ == "__main__":
    main()    


