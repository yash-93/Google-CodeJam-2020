import numpy as np

T = int(input())

for case in range(T):
	Mat = []
	size = int(input())

	for _ in range(size):
		row = list(map(int,input().split()))[:size] 
		Mat.append(row)

	diag_ele = np.array(Mat).diagonal()
	k = sum(diag_ele)

	print(f"Case #{case}: {k} {case} {case}")