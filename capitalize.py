def capitalize(string):
	l = string.split(' ')
	return ' '.join([i.capitalize() for i in l])
    
string = input()
c = capitalize(string)
print(c)

#' '.join([word.capitalize() for word in input().split(' ')])

