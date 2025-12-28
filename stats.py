
def get_book_text(filepath):
    #opens the text at the filepath provided, reads and returns the contents as string.
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents


def get_words(book_text):
    #prints total number of words to the console
    words = book_text.split()
    num_words = len(words)
    print(f"Found {num_words} total words")


def get_characters(book_text):
    #returns a dictionary acting as a histogram for characters, dictionary is of type {str : int}
    characters_list = []
    characters_dict = {}

    for character in book_text:
        if character.lower() in characters_list:
            characters_dict[character.lower()] += 1
        else:
            characters_list.append(character.lower())
            characters_dict.update({character.lower():1})
    
    return characters_dict



def sort_dict(dictionary_to_sort):
    list_of_dictionaries = []
    
    for key in dictionary_to_sort:
        list_of_dictionaries.append({"char": key, "num" : dictionary_to_sort[key]})

    def sort_on(items):
        return items["num"]


    list_of_dictionaries.sort(reverse=True, key=sort_on)

    return list_of_dictionaries
