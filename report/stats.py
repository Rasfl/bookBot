total_words_dict: dict[str, int] = {}
empty = 0
vowel: tuple[str, int] = []
# ---

def get_book_text(filepath: str):
    with open(filepath) as f: 
        text_book = f.read()
        return text_book
# ---

def count_nums(file_contents: str) -> int:
    total_words = file_contents.split()
    return len(total_words)
# ---

def count_character(total_words: list[str], empty: int):
    total_words_dict[" "] = empty
    for words in total_words:
        letter_words = words.lower()
        for letter in letter_words:
            if letter not in total_words_dict:
                total_words_dict[letter] = 1
            else:
                total_words_dict[letter] += 1
    return total_words_dict
# ---

def sort_on(sorted_chars):
    return sorted_chars[1]
# ---

def chars_dict_to_sorted_list(total_words_dict: dict[str, int]) -> list[tuple[str, int]]:
    temp_chars: list[tuple:[str, int]] = []
    for words in total_words_dict:
        temp_chars.append((words, total_words_dict[words]))
    sorted_chars = sorted(temp_chars, reverse=True, key=sort_on)
    return sorted_chars
# ---

def sorted_chars(filepath):
    file_contents = get_book_text(filepath)
    empty = file_contents.count(" ")
    num_words = count_nums(file_contents)
    total_words = file_contents.split()
    count_character(total_words, empty)
    # print(f"Found {num_words} total words")
    return chars_dict_to_sorted_list(total_words_dict), num_words

