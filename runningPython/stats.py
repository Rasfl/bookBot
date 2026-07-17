filepath = "books/frankenstein.txt"
total_words_dict: dict[str, int] = {}
empty = 0
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

def count_character(total_words: list[str], empty: int) -> None:
    total_words_dict[" "] = empty
    for words in total_words:
        letter_words = words.lower()
        for letter in letter_words:
            if letter not in total_words_dict:
                total_words_dict[letter] = 1
            else:
                total_words_dict[letter] += 1
    print(total_words_dict) 
# ---

def main():
    file_contents = get_book_text(filepath)
    empty = file_contents.count(" ")
    num_words = count_nums(file_contents)
    total_words = file_contents.split()
    count_character(total_words, empty)
    print(f"Found {num_words} total words")

main()