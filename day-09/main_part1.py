FILENAME = 'data.txt'

def load_input():
  content = None
  with open(FILENAME, 'r') as f:
    content = f.read()

  return content.splitlines()

def create_pyuramide_of_differences(record):
  difference_pyramide = []
  difference_pyramide.append(record)
  level = 0
  while True:
    next_row = []

    for i in range(len(difference_pyramide[level])):
      if i == len(difference_pyramide[level]) - 1:
        if len(next_row) == 0:
          next_row.append(0)

        difference_pyramide.append(next_row)
        break
      
      value = difference_pyramide[level][i] - difference_pyramide[level][i+1]
      next_row.append(abs(value))

    level += 1

    if sum(difference_pyramide[level]) == 0:
      break

    if level == len(difference_pyramide):
      break

  return difference_pyramide[::-1]

def predict_next_value(record):
  difference_pyramide = create_pyuramide_of_differences(record)
  levels = len(difference_pyramide)

  for i in range(levels):
    if i == levels - 1:
      break

    last_value = difference_pyramide[i][-1]
    next_row_last_value = difference_pyramide[i + 1][-1]

    if i == levels - 2 and next_row_last_value < difference_pyramide[i + 1][-2]:
      next_value = next_row_last_value - last_value
    else: 
      next_value = last_value + next_row_last_value

    difference_pyramide[i + 1].append(next_value)

  print(difference_pyramide[-1])

  return difference_pyramide[levels - 1][-1]


def predict_next_values(records):
  result = []

  for record in records:
    record = list(map(int, record.split(' ')))
    result.append(predict_next_value(record))

  return result

def main():
  input_data  = load_input()
  result      = predict_next_values(input_data)

  print(sum(result))

if __name__ == "__main__":
  main()