def prime_num_gen(n):
	prime_number_list =[]
	for num in range (0, int(last)):
		if check_if_prime(num) == true:
			prime_number_list.append(num)
		return prime_number_list


def check_if_prime(n):
	if (n==2) or (n==3):
		return True
	if n<=1:
		retun False
	for i in range(3,n):
		if (n%2 == 0) or (n%3 == 0) or (n%1 == 0):
			return False
		else:
			return True
			
print(prime_num_gen(20))