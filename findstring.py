s = "ABCDCDC"
ss = "CDC"
c, i, f = 0, 0, 1

while f:
	ind = s.find(ss)
	if ind != -1:
		s = s[ind+1:]
		c += 1
	else:
		f = 0
	
print(c)


def count_substring(string, sub_string):
    c, i, f = 0, 0, 1

    while f:
        ind = string.find(sub_string)
        if ind != -1:
            string = string[ind+1:]
            c += 1
        else:
            f = 0
    return c