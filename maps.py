n = int(input())
d = {}

for i in range(n):
	s = input().split()
	d[s[0]] = s[1]

print(d)

#inp = input()
q = []
#while inp != "":
while True:
	inp = input()
	if inp != '':
		q.append(inp)
	else:
		break

for i in q:
	if i in d:
		print(i+"="+d[i])
	else:
		print("Not found")

