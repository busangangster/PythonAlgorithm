import sys
input = sys.stdin.readline

word = input().strip()
words= []

for i in range(1,len(word)-1):
  for j in range(i+1,len(word)):
    a = word[:i]
    b = word[i:j]
    c = word[j:]

    a = a[::-1]
    b = b[::-1]
    c = c[::-1]

    words.append(a+b+c)

words.sort()
print(words[0])