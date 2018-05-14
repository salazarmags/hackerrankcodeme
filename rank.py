n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))


rx, ry = [{i: k for i, k in zip(sorted(z),range(1,len(z)+1))} for z in [x,y]]

d2 = [(rx[t] - ry[v])**2 for t, v in zip(x,y)]

print(round(1 - (6*sum(d2)) / (n*(n**2 - 1)), 3))