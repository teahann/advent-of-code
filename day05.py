
# with open('day05_example.txt') as file:
with open('day05.txt') as file:
  data = file.read()

parts = data.split('\n\n')

seeds = list(map(int, parts[0].split(': ')[1].split()))

def read_map(mapping):
  return [tuple(map(int, line.split())) for line in mapping.strip().split('\n')[1:]]

def apply_map(source, mapping):
  for dest_start, src_start, length in mapping:
    if src_start <= source < src_start + length:
      return dest_start + (source - src_start)
  return source

mappings = [read_map(part) for part in parts[1:]]

def lowest_location(seeds, mappings):
  result = []
  for seed in seeds:
    for map_type in mappings:
      seed = apply_map(seed, map_type)
    result.append(seed)
  return min(result)

print(lowest_location(seeds, mappings))
