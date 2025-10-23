from stats import number_words , number_characters , sort_counts

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    char_num = {}
    text = get_book_text("books/frankenstein.txt")
    #print(f"Found {number_words(text)} total words")
    char_num = number_characters(text)
    sorted_list = sort_counts(char_num)
    #print(sorted_list)

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