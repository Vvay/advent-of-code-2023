import re

FILENAME = 'untitled'
RE = '\d'

def get_file_content():
  content = None
  with open(FILENAME, 'r') as f:
      content = f.read()

  return content

def find_calibration_value(line):
  matches = re.findall(RE, line)
  first_digit = matches[0]
  last_digit = matches[-1]
        
  value = int(str(first_digit) + str(last_digit))

  return value

def process_input_file():
  lines = get_file_content().splitlines()
  result = []
  for line in lines:
    result.append(find_calibration_value(line))

  return result

def sum_calibration_values(calibration_values):
  return sum(calibration_values)

def main():
  calibration_values = process_input_file()
  total_sum  = sum_calibration_values(calibration_values)

  print(total_sum)

if __name__ == "__main__":
  main()