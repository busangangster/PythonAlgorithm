t = int(input())
for tc in range(1,t+1):
    n = int(input())
    dic = {}
    arr = list(map(int,input().split()))
    for x in arr:
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 1
    result = sorted(dic.items(),key = lambda x:(x[1],x[0]),reverse=True)
    print("#{} {}".format(n,result[0][0]))
      