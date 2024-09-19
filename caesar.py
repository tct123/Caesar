import string


def caesar(text):
    text = text.lower()
    abc = string.ascii_lowercase
    abclist = []
    for letter in abc:
        abclist.append(letter)
    texts = text.split(" ")
    letterlist = []
    for text in texts:
        for letter in text:
            letterlist.append(abclist[slice(letter)])
    text = ""
    for letter in letterlist:
        print(letter)
        # text.join(letter)
    return text


if __name__ == "__main__":
    print(caesar(text="Hallo Welt"))
