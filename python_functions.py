def sum_to(n):
  sum = 0
  for nums in range(1, n + 1):
    sum += nums
  return sum
print('Number 1')
print(sum_to(6))

def largest(list):
  biggest = 0
  for highest in list:
    if biggest < highest:
      biggest = highest
  return biggest

print('Number 2')
print(largest([1, 2, 3, 4, 0]))  # returns 4
print(largest([10, 4, 2, 231, 91, 54]))# returns 231

def occurrences(str, target):
  count = 0
  for letter in str:
    if letter == target:
      count+=1
      break
  if target in str:
    count+=1
  return count


print('Number 3')
print(occurrences('fleep floop', 'e'))  # returns 2
print(occurrences('fleep floop', 'p'))  # returns 2
print(occurrences('fleep floop', 'ee'))  # returns 1
print(occurrences('fleep floop', 'fe'))  # returns 0