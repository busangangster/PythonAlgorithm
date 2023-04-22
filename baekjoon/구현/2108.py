import sys
input = sys.stdin.readline

n = int(input())
nums = []
tt = []
gg = []
for _ in range(n):
  nums.append(int(input()))

nums.sort()
print(round(sum(nums)/n))
print(nums[len(nums)//2])

for i in nums:
  tt.append(nums.count(i))
  if nums.count(i) < max(tt):
    tt.remove(nums.count(i))
  
for i in nums:
  if i in gg:
    continue
  if max(tt) == nums.count(i):
    gg.append(i)

if len(gg) == 1:
  print(gg[0])
else:
  print(gg[1])


print(nums[-1] - nums[0])