import json
import random
import heapq

random.seed(0)

# Creates a list of size len, returns unique random numbers
def random_list(len):
  arr = random.sample(range(0, 15000), len)
  return arr

# Creates a list where all elements are at most k positions away from correct pos
# Uses a min heap
def nearly_sorted_list(len, k):
  arr = random.sample(range(0, 15000), len)
  pq = []
  # Push first k elements
  for i in range(k):
    heapq.heappush(pq, arr[i])
  i = k
  index = 0
  while i < len:
    heapq.heappush(pq, arr[i])
    # Size becomes k+1, pop and add min element in index pos
    arr[index] = heapq.heappop(pq)
    i += 1
    index += 1

  # Put the rest of the elements in array
  while pq:
    arr[index] = heapq.heappop(pq)
    index += 1
  return arr

# Creates a reversely sorted list with unique numbers
def reverse_list(len):
  arr = random.sample(range(0, 15000), len)
  arr.sort()
  arr.reverse()
  return arr

# Creates a list of size len, includes logic for heavy duplicates
def heavy_duplicate_list(len):
  if len <= 10:
    arr = [random.randint(1, 3) for _ in range(len)]
  elif len <=  100:
    arr = [random.randint(1, 10) for _ in range(len)]
  elif len <= 1000:
    arr = [random.randint(1, 100) for _ in range(len)]
  else:
    arr = [random.randint(1,500) for _ in range(len)]
  return arr

x = random_list(10)
print(x)
x = heavy_duplicate_list(10)
print(x)
x = reverse_list(10)
print(x)
x = nearly_sorted_list(10, 2)
print(x)