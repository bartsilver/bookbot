import sys
from stats import get_num_words
from stats import get_num_characters
from stats import sort_dictionary

def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]


    book_text = get_book_text(book_path)
    word_count = get_num_words(book_text)
    character_count = get_num_characters(book_text)
    sorted_character_count = sort_dictionary(character_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("----------- Character Count ----------")
    #print(character_count)
    for char_dict in sorted_character_count:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['count']}")
    print("============= END ===============")

main()
