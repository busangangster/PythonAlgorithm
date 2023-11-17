def solution(s):
    stack = []
    for x in s:
        if x == '(': # x가 '('시 무조건 append
            stack.append(x)
        else: # 아닐 경우
            if not stack: # 스택이 비어있으면, 즉 ')'이 stack의 처음 문자이면
                          # 괄호가 올바르게 짝지어 질 수 없기에 False
                return False
            
            if stack[-1] =='(': # 스택의 마지막 문자가 '('이면
                                # 짝지어서 스택에서 pop
                stack.pop()
    # 스택이 비어있으면 true, 아니면 flase
    if stack:
        return False
    else:
        return True

    
    

    
    