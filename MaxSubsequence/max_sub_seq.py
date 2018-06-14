from __future__ import print_function
def max_sub_seq(arr):
	if not arr:
		return []
	start = 0
	end = 0
	S = None
	max_s = None
	for idx, v in enumerate(arr):
		# print(idx, v)
		if S is None:
			S = v
			max_s = v
			end = idx
		else:
			S += v
			if (S >= max_s):
				end = idx
				max_s = S
			# print('end:', end, ', S: ', S)

	print('intermediate: ', arr[start:end+1])
	S=max_s
	for ii in range(end+1):
		S -= arr[ii]
		if (max_s<S):
			start = ii + 1			
			max_s = S
			# print ('start:', start, ', max:', max_s)

	# print(start, end)
	return arr[start:end+1]

if __name__ == '__main__':
	print(max_sub_seq([1,1,   -2, 3]))
	print(max_sub_seq([-2,1,-3, -4,-1,2,1,-5,4]))
	print(max_sub_seq([-2,1,-3, 4,-1,2,1,-5,4]))