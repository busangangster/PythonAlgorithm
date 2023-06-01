# 오큰수: 해당 숫자보다 큰 수 중 제일 먼저 해당되는 수
# ex) 5,10,9,16 => 5의 오큰수는 10 
# for문을 사용하면 시간초과 뜸 
# stack으로 풀어야 함 

import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
stack = []
ans = [-1] * n

# stack에 값을 넣는 것이 아닌 인덱스를 활용해야 함. 
# stack이 비어있지 않고, 스택의 마지막 값보다 반복문을 도는 값이 더 크다면
# 아닐 때까지 stack맨 뒤의 수를 pop하고 해당 인덱스를 가지고 있는 
# 값을 ans에 추가해줌 
for i in range(n):
    while stack and a[stack[-1]] < a[i]:
        ans[stack.pop()] = a[i]
    stack.append(i)

print(*ans)



