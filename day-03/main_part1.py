import re

FILENAME = 'data.txt'

def load_file_to_matrix():
  matrix = []
  with open(FILENAME, 'r') as f:
    for line in f.readlines():
      matrix.append(list(line))

  return matrix

def array_to_str(array_data):
  return ''.join(str(x) for x in array_data)

def special_character_in_neighbors(matrix, neighbors_range):
  x_start, x_end, y_start, y_end = neighbors_range
  for i in range(y_start, y_end):
    for j in range(x_start, x_end):
      if re.search(r'[^\d.\n]', matrix[i][j]) != None:
        return True

  return False

def get_neighbors_range(number, matrix, row_id):
  x_pos, length, _ = number
  x_start = x_pos if x_pos == 0 else x_pos - 1
  x_end   = x_pos + length if x_pos + length == len(matrix[0]) else x_pos + length + 1
  y_start = row_id if row_id == 0 else row_id - 1
  y_end   = row_id + 2 if row_id + 2 < len(matrix) else row_id + 1

  return (x_start, x_end, y_start, y_end)

def extract_part_numbers(numbers, matrix, row_id):
  result = []
  for number in numbers:
    neighbors_range = get_neighbors_range(number, matrix, row_id)
    if special_character_in_neighbors(matrix, neighbors_range):
      result.append(number[2])

  return result

def get_numbers_from_row(row):
  row_str = array_to_str(row)
  result = []
  for match in re.finditer(r'\d+', row_str):
    result.append((match.start(), match.end() - match.start(), int(match.group())))

  return result

def process_data(matrix):
  row_lenghth = len(matrix[0])
  result = []
  for row_id, row in enumerate(matrix):
    numbers_in_row      = get_numbers_from_row(row)
    part_numbers_in_row = extract_part_numbers(numbers_in_row, matrix, row_id)
    result.extend(part_numbers_in_row)

  return result

def main():
  matrix        = load_file_to_matrix()
  part_numbers  = process_data(matrix)
  total_sum     = sum(part_numbers)

  print(total_sum)

if __name__ == "__main__":
  main()