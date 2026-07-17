filepath = "books/frankenstein.txt"

def get_book_text(filepath: str):
    with open(filepath) as f: 
        text_book = f.read()
        return text_book

def count_nums(file_contents: str) -> int:
    return len(file_contents.split())

def main():
    file_contents = get_book_text(filepath)
    num_words = count_nums(file_contents)
    print(f"Found {num_words} total words")

main()