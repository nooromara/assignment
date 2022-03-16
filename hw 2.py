from urllib.request import urlopen

url = "https://www.gutenberg.org/files/11/11-0.txt"
# alice in wonderland by lewis carrol
local_name = "alice.txt"
import certifi
import ssl


def save_locally():
    """
    Save the book locally, so we can use it faster and no need to load every time
    :return: None
    """
    with open(local_name, "w") as local_fp:
        with urlopen(url, context=ssl.create_default_context(cafile=certifi.where())) as fp:
            for line in fp:
                line = line.decode('utf-8-sig').replace("\n", "")
                local_fp.write(line)


punctuation = ",;!.?-()"
def get_unique_words():
    """
    Get the dictionary of unique words and their frequency
    :return: dict
    """
    unique_words = {}
    with open(local_name) as fp:
        for line in fp:
            # remove punctuation
            for p in punctuation:
                line = line.replace(p, " ")
            line = line.lower()
            # get the words:
            for word in line.split():
                unique_words[word] = unique_words.get(word, 0) + 1

    return unique_words


save_locally()
unique_words = get_unique_words()
most_frequent = list(unique_words.values())
most_frequent.sort(reverse=True)
# print(most_frequent)
for word_frequency in most_frequent[:10]:
    for unique_word, value in unique_words.items():
        if word_frequency == value:
            print(f"common word '{unique_word}' appears {value} times")
            # change the value so we don't get it again if there are multiple words with the same frequency
            unique_words[unique_word] = -1
            break
unique_word_count = len(unique_words)
print("The number of unique words in Alice in Wonderland is: " + str(unique_word_count))

from urllib.request import urlopen

url = "https://www.gutenberg.org/cache/epub/64317/pg64317.txt"
# The Great Gatsby, by F. Scott Fitzgerald
local_name = "great gatsby.txt"
import certifi
import ssl


def save_locally():
    """
    Save the book locally, so we can use it faster and no need to load every time
    :return: None
    """
    with open(local_name, "w") as local_fp:
        with urlopen(url, context=ssl.create_default_context(cafile=certifi.where())) as fp:
            for line in fp:
                line = line.decode('utf-8-sig').replace("\n", "")
                local_fp.write(line)


punctuation = ",;!.?-()"
def get_unique_words():
    """
    Get the dictionary of unique words and their frequency
    :return: dict
    """
    unique_words = {}
    with open(local_name) as fp:
        for line in fp:
            # remove punctuation
            for p in punctuation:
                line = line.replace(p, " ")
            line = line.lower()
            # get the words:
            for word in line.split():
                unique_words[word] = unique_words.get(word, 0) + 1

    return unique_words


save_locally()
unique_words = get_unique_words()
most_frequent = list(unique_words.values())
most_frequent.sort(reverse=True)
# print(most_frequent)
for word_frequency in most_frequent[:10]:
    for unique_word, value in unique_words.items():
        if word_frequency == value:
            print(f"common word '{unique_word}' appears {value} times")
            # change the value so we don't get it again if there are multiple words with the same frequency
            unique_words[unique_word] = -1
            break

unique_word_count = len(unique_words)
print("The number of unique words in The Great Gatsby is: " + str(unique_word_count))
if unique_word_count > unique_word_count:
    print("The Great Gatsby has more distinct words than Alice in Wonderland")
elif unique_word_count < unique_word_count:
    print("Alice in Wonderland has more distinct words than The Great Gatsby")
else:
    print("Both books have the same amount of distinct words")