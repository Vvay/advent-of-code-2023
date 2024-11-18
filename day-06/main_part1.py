import math

FILENAME = 'data.txt'

def load_input():
  content = None
  with open(FILENAME, 'r') as f:
    content = f.read()

  return content.splitlines()

def extract_data(races_data):
  _, times      = races_data[0].split(':')
  times         = times.strip().split(' ')
  times         = list(filter(None, times))
  times         = [int(time) for time in times]
  _, distances  = races_data[1].split(':')
  distances     = distances.strip().split(' ')
  distances     = list(filter(None, distances))
  distances     = [int(distance) for distance in distances]

  return times, distances

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

def process_races(races_data):
  times, distances  = extract_data(races_data)
  result = []

  for i in range(len(times)):
    better_distances = get_nof_better_races(times[i], distances[i])
    result.append(better_distances)

  return result

def main():
  races_data  = load_input()
  best_races  = process_races(races_data)
  result      = math.prod(best_races)

  print(result)

if __name__ == "__main__":
  main()