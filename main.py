def main():
    print(" --- Begin report of books/frankenstein.txt --- ")
    contents = get_contents("books/frankenstein.txt")
    num_of_words = count_words(contents)
    letter_count = count_letters(contents)
    print(f"There are {num_of_words} words in the document")
    
    for letter, count in letter_count.items():
        if letter.isalpha() == True:
            print(f"The '{letter}' appears {count} times")

def count_words(text):
    words = text.split()
    
    word_count = len(words)

    return word_count


def get_contents(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
    
def count_letters(text):
    char_and_num = {}

    for char in text.lower():
        if char in char_and_num:
            char_and_num[char] +=1
        else:
            char_and_num[char] = 1
    return char_and_num 


main()



