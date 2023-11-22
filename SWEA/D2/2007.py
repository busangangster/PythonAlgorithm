t = int(input())
for t_case in range(1,t+1):
  s = input().strip()
  
  for i in range(1,len(s)):
    pattern = s[:i]

    if s[i:i+len(pattern)] == pattern:
      print('#{} {}'.format(t_case,len(pattern)))
      break