
# import sys

# n = sys.stdin.readline().strip()

# if n == n[::-1]:
#   print(1)
# else:
#   print(0)


import heapq as hq

a = [[1,2],[3,4]]
b = []

b.append(hq.heappop(a)[1])

print(b)