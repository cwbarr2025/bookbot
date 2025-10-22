def number_words(text):
    words = text.split()
    return len(words)

def number_characters(text):
    char_num = {} #empty dictionary
    chars = [] #empty list to store the individual characters
    words = text.split() #split the full text up into a list of individual words
    for word in words: #iterate through each word in the list
        word = word.lower() #makes all the characters in the string lowercase
        chars.append(list(word)) #list() seperates a string/word into it's individual characters
    for i in chars: #iterates through my list of lists
        for char in i: #iterates through each character in the list
            if char in char_num: #checks if the specific character is in my dictionary yet
                char_num[char] += 1 # adds 1 to the value of the key if it already exists
            else:
                char_num[char] = 1 # creates the key and sets the value to 1 if it does not exist yet
    return char_num