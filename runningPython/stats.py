filepath = "books/frankenstein.txt"
total_words_dict: dict[str, int] = []

def get_book_text(filepath: str):
    with open(filepath) as f: 
        text_book = f.read()
        return text_book
# ---

def count_nums(file_contents: str) -> int:
    total_words =  file_contents.split()
    return len(total_words)
# ---

def count_character(total_words):
    for words in total_words:
        letter_words = words.lower().split()
        for letter in letter_words:
            total_words_dict = {letter: 0}
            if letter in total_words_dict:
                total_words_dict[letter] += 1
    print(total_words_dict)
    return 

# ---
def main():
    file_contents = get_book_text(filepath)
    num_words = count_nums(file_contents)
    total_words = file_contents.split()
    count_character(total_words)
    print(f"Found {num_words} total words")

main()