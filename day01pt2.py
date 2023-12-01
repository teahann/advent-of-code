import re

example = [ 
  'two1nine',
  'eightwothree',
  'abcone2threexyz',
  'xtwone3four',
  '4nineeightseven2',
  'zoneight234',
  '7pqrstsixteen'
]

nums_key = {
  'zero': '0',
  'one': '1',
  'two': '2',
  'three': '3',
  'four': '4',
  'five': '5',
  'six': '6',
  'seven': '7',
  'eight': '8',
  'nine': '9'
}

with open('day01.txt') as file:
  lines = [line.rstrip('\n') for line in file]

# xtwone3four and zoneight234 should return x2134 and z18234
def normalize_digits(strings_list):
  normalized_strings = list(strings_list)
  for i, s in enumerate(normalized_strings):
    for word, digit in nums_key.items():
      pattern = r'\b' + word + r'\b'
      normalized_strings[i] = re.sub(pattern, digit, normalized_strings[i], flags=re.IGNORECASE)
  return normalized_strings

def extract_nums(string_list):
  nums = []
  for text in string_list:
    digits = re.findall(r'\d', text)
    if digits:
      first = digits[0] 
      last = digits[-1]
    nums.append((first, last))
  return nums

def calc_total(nums_list):
  total = 0
  for items in nums_list:
    total += int(''.join(items))
  return total

def calibration_value(data):
  normalized = normalize_digits(data)
  print(normalized)
  extracted_nums = extract_nums(normalized)
  total_sum = calc_total(extracted_nums)
  return total_sum

print(calibration_value(example))
# print(calibration_value(lines))
