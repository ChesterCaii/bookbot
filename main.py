import sys
from stats import get_words, count_chars, dict_to_sorted_list
def main():
	print("============ BOOKBOT ============")
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	print(f"Analyzing book found at {sys.argv[1]}.")
	print("----------- Word Count ----------")
	text = get_book_text(sys.argv[1])
	gotword = get_words(text)
	print(f"Found {gotword} total words") 

	print("--------- Character Count -------")
	getchars = count_chars(text)
	sorted_list = dict_to_sorted_list(getchars)
	for item in sorted_list:
		if item["char"].isalpha():
			print(f"{item['char']}: {item['num']}")
	print("============= END ===============")
def get_book_text(path_to_file):
	with open(path_to_file) as f:
		reader = f.read()
	return reader
main()



