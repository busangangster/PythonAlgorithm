
# 마을이 원형으로 되어 있기 때문에 한방향으로만 이동한다는 것이 포인트
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

# 최소 비용으로 모든 마을을 관광하는 경우는
# 이동 비용이 가장 비싼 마을을 거치지 않고 이동하는 경우
# 이동 비용을 모두 합한 값 - 이동 비용이 최대인 값
# => 최소 경비로 이동
print(sum(a)-max(a))


