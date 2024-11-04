import re

content = 'seeds: 79 14 55 13\n\nseed-to-soil map:\n50 98 2\n52 50 48\n\nsoil-to-fertilizer map:\n0 15 37\n37 52 2\n39 0 15\n\nfertilizer-to-water map:\n49 53 8\n0 11 42\n42 0 7\n57 7 4\n\nwater-to-light map:\n88 18 7\n18 25 70\n\nlight-to-temperature map:\n45 77 23\n81 45 19\n68 64 13\n\ntemperature-to-humidity map:\n0 69 1\n1 0 69\n\nhumidity-to-location map:\n60 56 37\n56 93 4'

seeds = re.search('(seeds:(\s\d+)*)', s).group()[7:].split(' ')
seeds = list(map(int, seeds))
seed_to_soil            = re.search('(seed-to-soil map:(\n\d+\s\d+\s\d+)*)',            content).group().splitlines()[1:]
soil_to_fertilizer      = re.search('(soil-to-fertilizer map:(\n\d+\s\d+\s\d+)*)',      content).group().splitlines()[1:]
fertilizer_to_water     = re.search('(fertilizer-to-water map:(\n\d+\s\d+\s\d+)*)',     content).group().splitlines()[1:]
water_to_light          = re.search('(water-to-light map:(\n\d+\s\d+\s\d+)*)',          content).group().splitlines()[1:]
light_to_temperature    = re.search('(light-to-temperature map:(\n\d+\s\d+\s\d+)*)',    content).group().splitlines()[1:]
temperature_to_humidity = re.search('(temperature-to-humidity map:(\n\d+\s\d+\s\d+)*)', content).group().splitlines()[1:]
humidity_to_location    = re.search('(humidity-to-location map:(\n\d+\s\d+\s\d+)*)',    content).group().splitlines()[1:]


print(humidity_to_location)