def minion_game(string):
	st, kv = 0, 0
	v ,l = "AEIOU" , len(string)

	kv = sum([l-i for i in range(l) if s[i] in v])
	st = l * (l + 1) // 2 - kv

	if kv > st: print("Kevin", kv)
	elif kv < st: print("Stuart", st)
	else: print("Draw")

s = input()
minion_game(s)


