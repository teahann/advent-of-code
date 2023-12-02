limits = {'red': 12, 'green': 13, 'blue': 14}

# Example data
example = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""".strip().split('\n')

# Question data
with open('day02.txt') as file:
  lines = [line.rstrip('\n') for line in file]

def qty_possible(games_input):
  possible_game_ids = []
  for game_line in games_input:
    game_id, reveals_raw = game_line.split(': ', 1)
    game_id = int(game_id.replace('Game ', ''))
    reveals = [r.strip() for r in reveals_raw.split('; ')]
    game_reveals = []

    for reveal in reveals:
      reveal_info = {}
      reveal_counts = reveal.split(', ')
      for count_color in reveal_counts:
        count, color = count_color.split(' ')
        # qty of each color
        reveal_info[color] = max(reveal_info.get(color, 0), int(count))
      game_reveals.append(reveal_info)
    if is_valid(game_reveals):
      possible_game_ids.append(game_id)
  
  return sum(possible_game_ids)

def is_valid(game_info):
  for reveal in game_info:
    for color, count in reveal.items():
      if count > limits[color]:
          return False
  return True

print(qty_possible(lines))