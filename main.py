def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    header = f"--- Begin report of {book_path} ---"
    print(header)
    book_report(text)
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)
    
def count_letters(text):
    count_dict = {}
    lower_text = text.lower()
    for char in lower_text:
        if char.isalpha():
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1
    return count_dict

def book_report(text):
    word_count = count_words(text)
    letter_count = count_letters(text)
    keys_list = list(letter_count.keys())
    keys_list.sort()

    print(f"{word_count} words found in the document")

    for i in keys_list:
        print(
            f"The '{i}' character was found {letter_count[i]} times"
        )



main()