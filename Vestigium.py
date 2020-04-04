import numpy as np
K = []
R = []
C = []

T = int(input())
if T >= 1 and T <= 100:
	for case in range(T):
		Mat = []
		N = int(input())
		r = 0
		c = 0
		k = 0
		break_flag = False
		if N >= 2 and N <= 100:
			for i in range(N):
				row = list(map(int,input().split()))[:N]
				for ele in row:
					if ele not in range(1, N+1):
						break_flag = True
				if break_flag == False:
					Mat.append(row)
					if len(row) != len(set(row)):
						r += 1
					k = k + row[i]
				else:
					break
		transpose = np.array(Mat).transpose()
		for j in range(N):
			if len(transpose[j]) != len(set(transpose[j])):
				c += 1
		K.append(k)
		R.append(r)
		C.append(c)
		
for ind in range(T):
	print(f"Case #{ind+1}: {K[ind]} {R[ind]} {C[ind]}")