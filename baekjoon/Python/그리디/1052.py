# 물병의 개수가 2진수 형태로 증가함
# 필요한 물병의 수는 이진수의 '1'의 개수임 

import sys
input = sys.stdin.readline

n, k = map(int,input().split())
cnt = 0


while bin(n).count('1') > k:
    res = bin(n)[::-1].index('1')
    cnt += 2**res
    n += 2**res

print(cnt)
