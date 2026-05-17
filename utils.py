import re


def read_classification_from_file(path):
    dict = {}
    with open(path, "r", encoding='utf-8') as f:
        for line in f.readlines():
            words = line.split()
            dict[words[0]] = words[1]
    return dict


def mail_cleaner(text):
    """
        Clean up email text by removing HTML tags, newline characters, tabs, quotes, extra spaces,
        and converting words to lowercase."""

    text = text.replace("\n", " ")

    cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    text = re.sub(cleanr, '', text)

    text = text.replace("\t", " ").replace('"'," ")

    while "  " in text:
        text = text.replace("  ", " ")

    word_arr = text.split(" ")
    while "" in word_arr:
        word_arr.remove("")


    word_arr = [word.lower() for word in word_arr]

    return " ".join(word_arr)

