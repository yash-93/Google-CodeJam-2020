T = int(input())

for i in range(T):
	s = input()
	s_list = []
	for i in s:
		if int(i) == 0:
			s_list.append(i)
		elif int(i) == 1:
			