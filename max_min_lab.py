def find_max_min(A):
	N = max(A)
	M = min(A)
	if M==N:
		return [len(A)]
	else:
		return[N,M]
		
print(find_max_min([2,24,25,26]))