def print_formatted(number):
	l = len(bin(number)[2:])
	for i in range(1, number +1 ):
		print(str(i).rjust(l,' '), str(oct(i)[2:]).rjust(l,' '), str(hex(i)[2:]).upper().rjust(l,' '), str(bin(i)[2:]).rjust(l,' '), sep = ' ')

n = int(input())
print_formatted(n)