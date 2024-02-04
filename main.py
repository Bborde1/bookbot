def count_words(text):
    counter = len(text.split())
    return counter


def get_letter_counts(text):
    pass


def main():
    book_path = "./books/frankenstein.txt"
    with open(book_path) as f:
        book_contents = f.read()
    print(count_words(book_contents))


main()
