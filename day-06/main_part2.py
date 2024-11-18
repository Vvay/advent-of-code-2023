import math

FILENAME = 'data.txt'

def load_input():
  content = None
  with open(FILENAME, 'r') as f:
    content = f.read()

  return content.splitlines()

def extract_data(race_data):
  _, time     = race_data[0].split(':')
  time        = time.strip().replace(' ', '')
  time        = int(time)
  _, distance = race_data[1].split(':')
  distance    = distance.strip().replace(' ', '')
  distance    = int(distance)

  return time, distance

def get_nof_better_races(time, distance):
  a = -1
  b = time
  c = -distance

  dis = (b * b) - (4 * a * c)
  sqrt_val = math.sqrt(abs(dis)) 
    
  if dis > 0: 
      x1 = ((-b + sqrt_val)/(2 * a))
      x1 = math.floor(x1)
      x2 = ((-b - sqrt_val)/(2 * a))
      x2 = math.floor(x2)

      return (x2 - x1)

  return 0

def process_race(race_data):
  time, distance   = extract_data(race_data)
  better_distances = get_nof_better_races(time, distance)

  return better_distances

def main():
  race_data = load_input()
  result    = process_race(race_data)

  print(result)

if __name__ == "__main__":
  main()