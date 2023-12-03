
example = [
  "467..114..",
  "...*......",
  "..35..633.",
  "......#...",
  "617*......",
  ".....+.58.",
  "..592.....",
  "......755.",
  "...$.*....",
  ".664.598.."
]

with open('day03.txt') as file:
  lines = [line.rstrip('\n') for line in file]

symbols = set()
for line in lines:
  for char in line:
    if not char.isdigit() and char != '.':
      symbols.add(char)

def get_adjacent(x, y, schematic):
  directions = [(-1, 0), (0, -1), (0, 1), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
  adjacent_cells = []
  for dx, dy in directions:
    new_x, new_y = x + dx, y + dy
    if 0 <= new_x < len(schematic[0]) and 0 <= new_y < len(schematic):
      adjacent_cells.append(schematic[new_y][new_x])
  return adjacent_cells

def check_part_number(start_x, end_x, y, schematic):
  for num_x in range(start_x, end_x):
    adjacent_cells = get_adjacent(num_x, y, schematic)
    if any(cell in symbols for cell in adjacent_cells):
      return True
  return False

def sum_part_numbers(schematic):
  sum_of_parts = 0
  for y, row in enumerate(schematic):
    x = 0
    while x < len(row):
      if row[x].isdigit():
        last_digit = x
        while last_digit < len(row) and row[last_digit].isdigit():
          last_digit += 1
        number = int(row[x:last_digit])
        if check_part_number(x, last_digit, y, schematic):
          sum_of_parts += number
        x = last_digit
      else:
        x += 1
  return sum_of_parts

print(sum_part_numbers(example))
print(sum_part_numbers(lines))
