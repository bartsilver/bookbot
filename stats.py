def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    character_count = {}
    for char in text:
        character_count[char.lower()] = character_count.get(char.lower(), 0) + 1
    return character_count 

def sort_dictionary(dictionary):
    sorted_list = []
    for char, count in dictionary.items():
        sorted_list.append({"char": char, "count": count})
    def sort_key(item):
        return item["count"]
    sorted_list.sort(reverse=True, key=sort_key)
    return sorted_list