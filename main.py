
path_frank = "books/frankenstein.txt"

def CharSortedList(CharDict):
    SortedList = []
    for ch in CharDict:
        SortedList.append({"char": ch, "num": CharDict[ch]})
    SortedList.sort(reverse=True, key=SortOn)
    return SortedList


def SortOn(dict):
    return dict["num"]

def Charac(text):
    Chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in Chars:
            Chars[lowered] += 1
        else:
            Chars[lowered] = 1
    return Chars

def CountWords(text):
    words = text.split()
    return len(words)

def book_text(path):
    with open(path) as f:
        return f.read()

def Main():
    text = book_text(path_frank)
    Words = CountWords(text)
    Letters = Charac(text)
    CharsSorted = CharSortedList(Letters)
    print(f"--Report-- {path_frank}")
    print(f"{Words} words found in the document")
    print()
    for item in CharsSorted:
        if not item["char"].isalpha():
            continue
        print(f" '{item['char']}' character was found {item['num']} times")
        print("--END--")
Main()
