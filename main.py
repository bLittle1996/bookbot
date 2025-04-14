from sys import argv
from stats import count_words, count_characters

        
PRINT_WIDTH = 40

def get_book_text(filepath: str) -> str:
    text = ""
    with open(filepath) as f:
        text = f.read()

    return text

def analyze_book(filepath):
    text = get_book_text(filepath)
    word_count = count_words(text)
    character_count = count_characters(text)
    characters = list(character_count.keys())
    # sort the characters by their values in the map
    characters.sort(key=lambda k: character_count.get(k) or 0, reverse=True)
    print(f"Analyzing book found at {filepath}...")
    print(" Word Count ".center(PRINT_WIDTH, "-"))
    print(f"Found {word_count} total words")
    print(" Character Count ".center(PRINT_WIDTH, "-"))
    
    for c in characters:
        if not c.isalpha():
            continue
        print(f"{c}: {character_count[c]}")
        
        
        
def main():
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return exit(1)


    print(" BOOK BOT ".center(PRINT_WIDTH, "="))
    analyze_book(argv[1])
    print(" END ".center(PRINT_WIDTH, "="))


main()

