n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))

from statistics import pstdev
x_ = sum(x)/len(x)
y_ = sum(y)/len(y)
x_s = pstdev(x)
y_s = pstdev(y)

print (round(sum([(i - x_)*(k - y_) for i, k in zip(x,y)]) / (n*x_s*y_s), 3 ))
