import sys
input = sys.stdin.readline

s,p = map(int,input().split())
sen = list(input().strip())
a,c,g,t = map(int,input().split())
dic = {'A':0,'C':0,'G':0,'T':0}
cnt = 0 
window = sen[:p]
for i in window:
  dic[i] += 1

if dic['A'] >= a and dic['C'] >= c and dic['G'] >= g and dic['T'] >= t:
  cnt += 1

for i in range(s-p):
  dic[sen[i]] -= 1
  dic[sen[p+i]] += 1

  if dic['A'] >= a and dic['C'] >= c and dic['G'] >= g and dic['T'] >= t:
    cnt += 1
print(cnt)