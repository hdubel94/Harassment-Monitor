word_list = [	'bad', 'bitch', 'crap', 'crazy', 'creepy', 'damn', 'dick', 'fag', 'fool', 'freak', 'fuck', 'gross', 'hit', 'idiot', 'kill', 'lose', 'nerd', 'never', 'no', 'out', 'poor', 'puss', 'retard', 'sex', 'shit', 'shut', 'slut', 'smack', 'stupid', 'suck', 'tits', 'ugly', 'weird', 'whore', 'worst', 'wrong',
				'and', 'about', 'almost', 'always', 'as', 'be', 'big', 'black', 'boy', 'could', 'day', 'doing', 'down', 'drink', 'early', 'face', 'feel', 'food', 'force', 'get', 'girl', 'give', 'gone', 'hello', 'high', 'hot', 'job', 'joke', 'know', 'late', 'left', 'little', 'long', 'low', 'man', 'men', 'mess', 'most', 'never', 'not', 'now', 'only', 'over', 'probably', 'say', 'short', 'should', 'soon', 'stick', 'straight', 'stuck', 'such', 'take', 'that', 'the', 'there', 'their', 'think', 'time', 'top', 'touch', 'up', 'want', 'way', 'what', 'when', 'where', 'which', 'why', 'with', 'woman', 'women', 'work', 'yeah', 'you',
				'best', 'creative', 'cool', 'fair', 'fine', 'fun', 'good', 'great', 'happy', 'help', 'luck', 'nice', 'please', 'right', 'smart', 'strong', 'thank', 'welcome', 'well', 'win', 'yes']

# Keyword check for positive/negative words
def phrase_to_hash(phrase):
	phrase = phrase.lower()
	current_hash = []
	for current_word in word_list:
		if current_word in phrase:
			current_hash += [1]
		else:
			current_hash += [0]
	return current_hash
