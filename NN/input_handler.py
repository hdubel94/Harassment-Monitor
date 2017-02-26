# Integer modulated and converted to binary list
def char_conversion(n):
	n = n % 7
	n = bin(n)[2:]
	while len(n) < 3:
		n = '0' + n
	n = list(n)
	n = [int(i) for i in n]
	return n

# Integer modulated and converted to binary list
def mod_conversion(n):
	n = n % 31
	n = bin(n)[2:]
	while len(n) < 5:
		n = '0' + n
	n = list(n)
	n = [int(i) for i in n]
	return n

# This needs to be carefully designed, returns zeros at the moment
def phrase_to_hash(phrase):
	current_hash = []
	char_count = {}
	primes = [2, 3, 5, 7, 11, 13, 17]
	mod_count = {}
	for i in range(32, 127):
		char_count[i] = 0
	for i in primes:
		mod_count[i] = 0
	for index, current_char in enumerate(phrase):
		char_count[ord(current_char)] += 1
		for i in primes:
			if index % i == 0:
				mod_count[i] += ord(current_char)
	for i in range(32, 127):
		current_hash += char_conversion(char_count[i])
	for i in primes:
		current_hash += mod_conversion(mod_count[i])
	return current_hash
