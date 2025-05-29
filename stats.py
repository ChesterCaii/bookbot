def get_words(text):
        words = text.split()
        num_words = len(words)
        return num_words

def count_chars(text):
	chars = {}
	for t in text:
		character = t.lower()
		if character not in chars:
			chars[character] = 1
		else:
			chars[character] += 1
	return chars

def sort_on(d):
        return d["num"]

def dict_to_sorted_list(chars):
	sorted_list = []
	for key, val in chars.items():
		d = {"char": key, "num":val}
		sorted_list.append(d)
	sorted_list.sort(reverse=True, key=sort_on)
	return sorted_list

