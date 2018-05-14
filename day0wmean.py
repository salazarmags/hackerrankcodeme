N = int(input())
X = list(map(int, input().split()))
W = list(map(int, input().split()))

if any( not(5 <= i <= 50) for i in [N,len(X),len(W)]):
    print("Number of elements must be between 5 and 50")
elif any( x <= 0 or w <= 0 or x > 100 or w > 100 for x, w in zip(X,W)):
    print("Elements must be between 0 and 100")
else:
    down = X[0:len(X)//2]
    up = X[(len(X)//2)+1:len(X)]


    if N % 2 == 0:
    median = (X[(N//2)-1] + X[N//2])/2
    else:
    median = X[((N+1)//2) - 1]

