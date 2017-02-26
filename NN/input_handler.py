word_list = [	'bad', 'bitch', 'crap', 'crazy', 'creepy', 'damn', 'dick', 'dumb, ''fag', 'fat', 'fool', 'freak', 'fuck', 'gross', 'hit', 'idiot', 'kill', 'lose', 'nerd', 'never', 'no', 'out', 'poor', 'puss', 'retard', 'sex', 'shit', 'shut', 'slap', 'slut', 'smack', 'stupid', 'suck', 'tits', 'ugly', 'weird', 'whore', 'worst', 'wrong',
				'and', 'any', 'about', 'almost', 'always', 'as', 'bag', 'ball', 'be', 'big', 'black', 'boy', 'cat', 'cold', 'could', 'day', 'dog', 'doing', 'down', 'drink', 'early', 'face', 'feel', 'food', 'force', 'forget', 'forgot', 'get', 'girl', 'give', 'gone', 'harass', 'have', 'hello', 'high', 'hot', 'job', 'joke', 'know', 'late', 'left', 'little', 'long', 'look', 'low', 'man', 'men', 'mess', 'most', 'need', 'never', 'not', 'now', 'only', 'outside', 'over', 'probably', 'rain', 'say', 'short', 'should', 'show', 'soon', 'stand', 'stick', 'straight', 'stuck', 'such', 'sun', 'take', 'that', 'the', 'there', 'their', 'think', 'time', 'top', 'touch', 'up', 'want', 'warm', 'way', 'weather', 'what', 'when', 'where', 'which', 'why', 'with', 'woman', 'women', 'work', 'yeah', 'you',
				'best', 'creat', 'cool', 'fair', 'fine', 'fun', 'good', 'great', 'happy', 'help', 'like', 'love', 'luck', 'nice', 'please', 'right', 'smart', 'strong', 'thank', 'welcome', 'well', 'win', 'yes']

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
