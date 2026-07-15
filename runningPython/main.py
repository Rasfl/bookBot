def get_book_text(filepath: str):
    with open(filepath) as f:
        file_contents = f.read()
    print(file_contents)
    return file_contents

filepath = "bookBot/runningPython/books/frankenstein.txt"

def main((get_book_text(filepath)):
    print(get_book_text(filepath))