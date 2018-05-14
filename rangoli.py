import string

n = int(input())


def rangoli(size):
	L = []
	for i in range(size):
		l = string.ascii_lowercase[i:size]
		'-'.join(l[::-1] + l[1:])
		L.append(('-'.join(l[::-1] + l[1:])).center(4*n-3,'-'))
	print('\n'.join(L[:0:-1]+L))

rangoli(n)
