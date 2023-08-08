import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  p = list(input().strip())
  n = int(input())
  a = input()
  a = a[1:-2]
  nums = []
  r = 0
  start = 0
  end = 0
  if len(a) != 0:
    nums = list(map(int,a.split(',')))
  flag = True

  for i in p:
    if i == 'R':
      r +=1 
      if flag:
        flag = False
      else:
        flag = True
    else:
      if flag == False:
        end += 1
      else:
        start += 1

  if start + end > len(nums):
    print('error')
  else:
    if r%2 == 0:
      nums = nums[start:len(nums)-end]
      print(f"[{','.join(map(str,nums))}]")
    else:
      nums = nums[start:len(nums)-end]
      nums = nums[::-1]
      print(f"[{','.join(map(str,nums))}]")