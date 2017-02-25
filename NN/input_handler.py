# This needs to be carefully designed, returns zeros at the moment
def phrase_to_hash(phrase):
	total = 0
	char_count = {}
	for i in range(32, 127):
		char_count[i] = 0
	for current_char in phrase:
		total += ord(current_char)
		char_count[ord(current_char)] += 1
	return [0] * 100
