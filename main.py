
def main():
    book_path = "books/frankenstein.txt"
    text = get_text_book(book_path)
    num_words = get_num_words(text)
    chars = get_chars_count(text)
    chars_list = chars_dict_to_sorted_list(chars)

    chars_list.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document {book_path}")
    print()

    for item in chars_list:
        if not item["char"].isalpha():
            continue

        print(f"The '{item['char']}' character was found {item['occurrences']} times")

    print("--- End report ---")
    
def get_text_book(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_count(text):
    chars = {}

    for char in text:
        char_lowered = char.lower()

        if char_lowered in chars:
            chars[char_lowered] += 1
        else:
            chars[char_lowered] = 1

    return chars

def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []

    for ch in chars_dict:
        sorted_list.append({"char": ch, "occurrences": chars_dict[ch]})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def sort_on(d):
    return d["occurrences"]

main()

