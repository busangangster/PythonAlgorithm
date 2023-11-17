
def solution(arr):
    stack = []
    stack.append(arr[0]) # 배열 arr의 첫 숫자를 stack에 append.
    for i in range(1,len(arr)): # 1부터 배열의 길이만큼 돌면서
        if arr[i] != stack[-1]: # 해당 숫자가 stack의 마지막 숫자와 일치 하지 않으면
            stack.append(arr[i]) #stack에 append
    return stack

