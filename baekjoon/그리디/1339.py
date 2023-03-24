import sys
n = int(sys.stdin.readline())
alphabet= [0 for _ in range(26)]

for _ in range(n):
  word = sys.stdin.readline().strip()
  for i in range(len(word)):
    alphabet[ord(word[i])-ord('A')] += 10 ** (len(word)-1-i)

alphabet.sort(reverse=True)
ans = 0
num = 9

for i in range(len(alphabet)):
  if alphabet[i] == 0:
    break
  ans += alphabet[i] * num
  num -= 1

print(ans)


