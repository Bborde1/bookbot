def count_words(text):
    counter = len(text.split())
    return counter


def get_letter_counts(text):
    text = text.lower()
    count_result = {}
    for letter in text:
        if letter.isalpha():
            if letter in count_result:
                count_result[letter] += 1
            else:
                count_result[letter] = 1
    return count_result


def generate_report(book_title, word_count, letter_counts):
    print(f"--- Begin report of {book_title}")
    print(f"There are a total of {word_count} words in this document.")
    sorted_letter_counts = sorted(
        letter_counts.items(), key=lambda x: x[1], reverse=True
    )
    for letter in sorted_letter_counts:
        print(f"The {letter[0]} character was found {letter[1]} times.")


def main():
    book_path = "./books/frankenstein.txt"
    with open(book_path) as f:
        book_contents = f.read()
    generate_report(
        book_path, count_words(book_contents), get_letter_counts(book_contents)
    )


main()
