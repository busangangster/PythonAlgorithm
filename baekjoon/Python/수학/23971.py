import sys
input = sys.stdin.readline

h,w,n,m = map(int,input().split())
cnt = 1
k = 1
t = 1
cnt1 = 0
cnt2 = 0
for i in range(2,w+1):
  if i - k > m:
    cnt1 += 1
    k = i

for i in range(2,h+1):
  if i - t > n:
    cnt2 += 1
    t = i

cnt += cnt1 + cnt2 + (cnt1*cnt2)
print(cnt)