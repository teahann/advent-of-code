example = [
  "Time:      71530",
  "Distance:  940200"
]

puzzle = [
  "Time:        61677571",
  "Distance:   430103613071150"
]

times = [int(x) for x in puzzle[0].split()[1:]]
distances = [int(x) for x in puzzle[1].split()[1:]]

def ways_to_win(duration, record):
  ways = 0
  for hold_time in range(1, duration):
    speed = hold_time
    travel_time = duration - hold_time
    distance = speed * travel_time
    if distance > record:
      ways += 1
  return ways

ways = 1
for duration, record in zip(times, distances):
  ways *= ways_to_win(duration, record)

print(ways)
