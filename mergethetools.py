def merge_the_tools(string, k):
 	p = len(string)//k
    s =	[string[i*k:(i+1)*k] for i in range(p)]

    for i in s:
        while len(i): 
            print(i[0],end="")
            i = i.replace(i[0],'')
    	print(" ")


string, k = input(), int(input()) 
merge_the_tools(string, k)