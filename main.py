from stats import number_words , number_characters , sort_counts
import sys #imports built in module sys so that the path to the textfile can be passed from terminal

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    char_num = {}
    try:
        text = get_book_text(sys.argv[1]) #passes the path to text to get_book_text
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    char_num = number_characters(text)
    sorted_list = sort_counts(char_num)
    print("============ BOOKBOT ============\n" #\n tells print to go to a new line in the terminal/output
          "Analyzing book found at books/frankenstein.txt...\n"
          "----------- Word Count ----------\n"
          f"Found {number_words(text)} total words")
    print("--------- Character Count -------")
    for dict in sorted_list: #iterates through my sorted list of dictionaries (char: .. , num: ..)
        if dict["char"].isalpha(): #checks character tied to the key "char" and returnes True if it is an alphebatical character
            print(f"{dict["char"]}: {dict["num"]}") #prints the char and the num to screen
    print("============= END ===============")


main()