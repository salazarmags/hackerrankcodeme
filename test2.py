N = int(input())
X = input()

X = X.split()

for i in range(len(X)):
    X[i] = float(X[i])

#mean
print sum(X)/N

#median
Xs = sorted(X)
if N % 2 == 0:
    print (Xs[(N/2)-1] + Xs[(N/2)])/2
elif N % 2 != 0:
    print Xs[((len(Xs)+1)/2)-1]

#mode

result = {}
for i in Xs:
    if i not in result:
        result[i] = 0
    result[i] += 1
    
for n, c in result.iteritems():
    print "{0}: {1}".format(n, c)

maxima = max(result.values())

for n, c in result.iteritems():
    if == max:
            
    print "{0}: {1}".format(n, c)



from collections import Counter
c = Counter(Xs)
maximo = max(c.values())

if all(i == maximo for i in result.values()):
    print result[0]
elif 




