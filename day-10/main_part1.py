FILENAME = 'data.txt'

def load_input():
  content = None
  with open(FILENAME, 'r') as f:
    content = f.read()

  return content

def process_input(input):
  start = None
  matrix = []
  lines = input.split('\n')

  for y, line in enumerate(lines):
    row = []
    for x, char in enumerate(line):
      if char == 'S':
          start = (x, y)
      row.append(char)
    matrix.append(row)

  return start, matrix

def map_road(start, matrix):
  x, y = start
  length = len(matrix)
  width = len(matrix[0])

  visited = []
  visited.append(start)

  if matrix[y][x + 1] == '-' or matrix[y][x + 1] == '7' or matrix[y][x + 1] == 'J':
    next_x = x + 1
    next_y = y

  elif matrix[y + 1][x] == '|' or matrix[y + 1][x] == 'L' or matrix[y + 1][x] == 'J':
    next_x = x
    next_y = y + 1

  elif matrix[y - 1][x] == '|' or matrix[y - 1][x] == 'L' or matrix[y - 1][x] == 'J':
    next_x = x
    next_y = y - 1

  while True:
    visited.append((next_x, next_y))
    if matrix[next_y][next_x] == 'J':
      break

    
  matrix[y][x] = 'S'
  return matrix


def find_coords(input):
  result = []
  start, matrix = process_input(input)


  return result

def main():
  input_data  = load_input()
  result      = find_coords(input_data)

  print(sum(result))

if __name__ == "__main__":
  main()