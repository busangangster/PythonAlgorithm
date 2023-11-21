import sys
input = sys.stdin.readline

card = []
num = []
cnt_card= {'R':0,'B':0,'Y':0,'G':0}
cnt_num = [0 for _ in range(10)]
ans = 0
for _ in range(5):
  a,b = map(str,input().split())
  card.append(a)
  cnt_card[a] += 1
  num.append(int(b))
  cnt_num[int(b)] += 1

num.sort()

# 1
if max(cnt_card.values()) == 5 and num[0] + 1 == num[1] and num[1] + 1 == num[2] and num[2] + 1 == num[3] and num[3] + 1 == num[4]:
    ans = 900 + num[4]

# 2
elif 4 in cnt_num:
  ans = 800 + cnt_num.index(4)

# 3
elif 3 in cnt_num and 2 in cnt_num:
  ans = 700 + cnt_num.index(3)*10 + cnt_num.index(2)

# 4
elif 5 in cnt_card.values():
  ans = 600 + max(num)

# 5
elif num[0] + 1 == num[1] and num[1] + 1 == num[2] and num[2] + 1 == num[3] and num[3] + 1 == num[4]:
  ans = 500 + num[4]
  
# 6
elif 3 in cnt_num:
  ans += 400 + cnt_num.index(3)

# 7,8
elif 2 in cnt_num:
  first = cnt_num.index(2)
  cnt_num[first] = 0
  if 2 in cnt_num:
    second = cnt_num.index(2)
    ans = max(first,second)*10 + min(first,second) + 300
  else:
    ans = first + 200

else:
  ans = max(num) + 100 

print(ans)
    