N = int(input())
X = sorted(list(map(int, input().split())))

if any( not(5 <= i <= 50) for i in [N,len(X)]):
    print("Number of elements must be between 5 and 50")
elif any( x <= 0 or x > 100 for x in X):
    print("Elements must be between 0 and 100")
else:
    
    down = X[0:len(X)//2]
    up = X[((len(X)//2)+1):len(X)]
    
    print((down[(len(down)//2)-1] + down[len(down)//2])//2)
    print(X[(len(X)//2)])
    print((up[(len(up)//2)-1] + up[len(up)//2])//2)

    
