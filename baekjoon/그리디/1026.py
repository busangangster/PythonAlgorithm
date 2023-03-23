n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
s = 0

# 가장 큰 값이랑 작은 값을 곱해주고, 리스트에서 제거
# 리스트에 남아 있는 값들로 반복문 실행
for _ in range(n):
  s += max(a)*min(b)
  a.remove(max(a))
  b.remove(min(b))

print(s)