import re

# example = [ '1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet' ]

with open('day01.txt') as file:
  lines = [line.rstrip('\n') for line in file]

def extract_nums(string_list):
  nums = []
  for text in string_list:
    digits = re.findall(r'\d', text)
    if digits:
      first = digits[0] 
      last = digits[-1]
    nums.append((first, last))
  return nums

def calc_sum(nums_list):
  total = 0
  for items in nums_list:
    total += int(''.join(items))
  return total

def calibration_value(data):
  extracted_nums = extract_nums(data)
  total_sum = calc_sum(extracted_nums)
  return total_sum

# print(calibration_value(example))
print(calibration_value(lines))
