def climbingLeaderboard(scores, alice):
    l=[];r=[]
    for i in scores:
        if i  not in l:
            l.append(i)
    l.sort(reverse=True)
    for v in alice:
        c= l + [v]
        c.sort(reverse=True)
        temp=c.index(v)
        r.append((temp+1))
        c.pop(temp)
    return r

scores_count = int(input())
scores = list(map(int, input().rstrip().split()))
alice_count = int(input())
alice = list(map(int, input().rstrip().split()))
result = climbingLeaderboard(scores, alice)
print(result)
