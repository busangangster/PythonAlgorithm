import sys
input = sys.stdin.readline

n,m = map(int,input().split())

bs = m**n % 1000000007 # 브실이가 근무를 서는 경우
no_bs = (m-1)**n  % 1000000007# 브실이 없이 근무 서는 경우 

print((bs - no_bs))

