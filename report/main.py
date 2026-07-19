# Start of imports
import sys
from stats import sorted_chars

def print_report(conteudo, filepath:str):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {conteudo[1]} total words")
    print("--------- Character Count -------")
    for temp_sorteed in conteudo[0]:
        if temp_sorteed[0].isalpha():
            print(f"{temp_sorteed[0]}: {temp_sorteed[1]}")
    print("============= END ===============")
    return

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath: str = sys.argv[1]
    conteudo = sorted_chars(filepath)
    print_report(conteudo, filepath)
    return

main()
