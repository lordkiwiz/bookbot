def main():
    frankenstein = "books/frankenstein.txt"
    text = get_text(frankenstein)
    print(text)
    wordcount = word_count(text)
    print(wordcount)
    character_count = get_character_count(text)
    print(character_count)
    create_report(character_count)


def get_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    charachters = {}
    for c in text:
        try:
            charachters[c.lower()] += 1
        except:
            charachters[c.lower()] = 1
    return charachters

def get_count(element):
    return element[1]

def create_report(dictionary):
    character_list = list(dictionary.items())
    character_list.sort(reverse=True, key=get_count)
    for character in character_list:
        if character[0].isalpha():
            print(f"The '{character[0]}' character was found {character[1]} times")

main()