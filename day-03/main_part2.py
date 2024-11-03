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

def get_neighbors_from_row(row, x_start, x_end):
  row_str = array_to_str(row)
  result  = []
  for match in re.finditer(r'\d+', row_str):
    if not ((match.end() - 1 < x_start) or (match.start() > x_end)):
      result.append(int(match.group()))

  return result

def extract_neighbors(matrix, neighbors_range):
  x_start, x_end, y_start, y_end = neighbors_range
  result = []
  for i in range(y_start, y_end + 1):
    neighbors = get_neighbors_from_row(matrix[i], x_start, x_end)
    if neighbors:
      result.extend(neighbors)

  return result

def get_neighbors_range(star_x_pos, matrix, row_id):
  x_start = star_x_pos if star_x_pos == 0 else star_x_pos - 1
  x_end   = star_x_pos if star_x_pos == len(matrix[0]) - 1 else star_x_pos + 1
  y_start = row_id if row_id == 0 else row_id - 1
  y_end   = row_id if row_id == len(matrix) - 1 else row_id + 1

  return (x_start, x_end, y_start, y_end)

def extract_gears(stars_in_row, matrix, row_id):
  result = []
  for star in stars_in_row:
    neighbors_range = get_neighbors_range(star, matrix, row_id)
    neighbors       = extract_neighbors(matrix, neighbors_range)
    if len(neighbors) == 2:
      result.append(neighbors)

  return result

def get_stars_from_row(row):
  row_str = array_to_str(row)
  result  = []
  for match in re.finditer(r'[*]', row_str):
    result.append((match.start()))

  return result

def get_gear_ratios_in_row(gear):
  result = []
  for gear in gear:
    result.append(int(gear[0])*int(gear[1]))

  return result

def process_data(matrix):
  row_lenghth = len(matrix[0])
  result = []
  for row_id, row in enumerate(matrix):
    stars_in_row = get_stars_from_row(row)
    gears_in_row = extract_gears(stars_in_row, matrix, row_id)
    if len(gears_in_row) > 0:
      gear_ratios_in_row = get_gear_ratios_in_row(gears_in_row)
      result.extend(gear_ratios_in_row)

  return result


def main():
  matrix      = load_file_to_matrix()
  gear_ratios = process_data(matrix)
  total_sum   = sum(gear_ratios)

  print(total_sum)

if __name__ == "__main__":
  main()
