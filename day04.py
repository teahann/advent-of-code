example = [
    "41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "31 18 13 56 72 | 74 77 10 23 35 67 36 11",
]

with open('day04.txt') as file:
  lines = [line.rstrip('\n') for line in file]

def calc_points(cards):
  total = 0
  
  for card in cards:
    winning_nums, card_nums = card.split(' | ')
    winning_nums = set(winning_nums.split())
    check_nums = card_nums.split()
    matches = 0
    points = 0
    for number in check_nums:
      if number in winning_nums:
        matches += 1
        points = 1 if matches == 1 else points * 2
    total += points

  return total

# print(calculate_card_points(example))
print(calc_points(lines))
