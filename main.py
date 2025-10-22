from stats import number_words , number_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    char_num = {}
    text = get_book_text("books/frankenstein.txt")
    print(f"Found {number_words(text)} total words")
    char_num = number_characters(text)
    print(char_num)

main()