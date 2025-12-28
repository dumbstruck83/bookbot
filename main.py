
from stats import get_words, get_book_text, get_characters, sort_dict
from pprint import PrettyPrinter

import sys

if not len(sys.argv) == 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    result = get_book_text(f"{sys.argv[1]}")

    print("----------- Word Count ----------")
    get_words(result)

    print("--------- Character Count -------")
    result_dict = get_characters(result)
    sorted_list_of_dicts = sort_dict(result_dict)

    for d in sorted_list_of_dicts:
        if d["char"].isalpha():
            print(f"{d["char"]}: {d["num"]}")
        else:
            continue

print(sys.argv)



main()
