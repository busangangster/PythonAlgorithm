import sys
input = sys.stdin.readline

a = int(input())
b = list(map(int,input().split()))

# 입력받은 리스트 b 안에는 n의 진짜 약수들만 들어있기 때문에
# 리스트의 max값과 min값을 곱했을 때 N을 구할 수 있음 
print(max(b)*min(b))



