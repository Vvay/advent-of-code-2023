import re

FILENAME = 'data.txt'

def load_file():
  content = None
  with open(FILENAME, 'r') as f:
    content = f.read()

  return content

def prepare_data(data_set):
  result = []
  for line in data_set:
    destination_range_start, source_range_start, range_length = line.split(' ')
    result.append((int(destination_range_start), int(source_range_start), int(range_length)))
  return result

def get_source_number(searched_value, data_set):
  for line in data_set:
    if searched_value >= line[1] and searched_value <= line[1] + line[2]:
      return line[0] + searched_value - line[1]

  return searched_value

def process_data(content):
  seeds = re.search('(seeds:(\s\d+)*)', content).group()[7:].split(' ')
  seeds = list(map(int, seeds))

  seed_to_soil            = re.search('(seed-to-soil map:(\n\d+\s\d+\s\d+)*)',            content).group().splitlines()[1:]
  seed_to_soil            = prepare_data(seed_to_soil)

  soil_to_fertilizer      = re.search('(soil-to-fertilizer map:(\n\d+\s\d+\s\d+)*)',      content).group().splitlines()[1:]
  soil_to_fertilizer      = prepare_data(soil_to_fertilizer)

  fertilizer_to_water     = re.search('(fertilizer-to-water map:(\n\d+\s\d+\s\d+)*)',     content).group().splitlines()[1:]
  fertilizer_to_water     = prepare_data(fertilizer_to_water)

  water_to_light          = re.search('(water-to-light map:(\n\d+\s\d+\s\d+)*)',          content).group().splitlines()[1:]
  water_to_light          = prepare_data(water_to_light)

  light_to_temperature    = re.search('(light-to-temperature map:(\n\d+\s\d+\s\d+)*)',    content).group().splitlines()[1:]
  light_to_temperature    = prepare_data(light_to_temperature)

  temperature_to_humidity = re.search('(temperature-to-humidity map:(\n\d+\s\d+\s\d+)*)', content).group().splitlines()[1:]
  temperature_to_humidity = prepare_data(temperature_to_humidity)

  humidity_to_location    = re.search('(humidity-to-location map:(\n\d+\s\d+\s\d+)*)',    content).group().splitlines()[1:]
  humidity_to_location    = prepare_data(humidity_to_location)

  locations = []
  for seed in seeds:
    soil        = get_source_number(seed, seed_to_soil)
    fertilizer  = get_source_number(soil, soil_to_fertilizer)
    water       = get_source_number(fertilizer, fertilizer_to_water)
    light       = get_source_number(water, water_to_light)
    temperature = get_source_number(light, light_to_temperature)
    humidity    = get_source_number(temperature, temperature_to_humidity)
    location    = get_source_number(humidity, humidity_to_location)

    locations.append((seed, location))

  return locations

def main():
  content       = load_file()
  locations     = process_data(content)
  min_location  = min(locations, key=lambda x: x[1])

  print(min_location)

if __name__ == "__main__":
  main()