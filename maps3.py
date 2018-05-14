n = int(input())
s = [input().split() for _ in range(n)]
d = {k: v for k,v in s}

q = []
while True:
    try:
        name = input()
        q.append(name)
    except:
        break

for i in q:
	if i in d:
		print(i+"="+d[i])
	else:
		print("Not found")

