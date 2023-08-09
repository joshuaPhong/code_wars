# sort a string
sentence_to_sort = "This7 will6 be5 the4 sentence3 we2 sort1"
list_of_words = []


def order(sentence):
    list_of_words = {}

    split_sentence = sentence.split(" ")
    for word in split_sentence:
        for char in word:
            if char.isdigit():
                digit = int(char)
                if digit not in list_of_words:
                    list_of_words[digit] = []
                list_of_words[digit].append(word)

    sorted_keys = sorted(list_of_words.keys())
    new_sentence = ""  # Initialize the new sentence

    for key in sorted_keys:
        words_for_digit = list_of_words[key]
        new_sentence += " ".join(words_for_digit) + " "

    return new_sentence.strip()  # Remove trailing whitespace


def order_sentence_by_digit(sentence):
    """
    This function orders a sentence by digits embedded in the words.
    It splits the sentence into words.
    it sorts the words using sorted() function
    The sorted() has a key will use a callback function
    :param sentence:
    :return: A print output of the sorted sentence
    """
    words_from_sentence = {}
    split_sentence = sentence.split(" ")
    sorted_sentence = sorted(split_sentence, key=extract_digit)
    print(" ".join(sorted_sentence))


def select_the_digit(word):
    return any(char.isdigit() for char in word)


def extract_digit(word):
    """
    Extracts the numeric portion of a word and returns it as an integer.
    If no numeric portion is found, returns a large number.
    """
    digits = ''.join(
        filter(str.isdigit, word))  # Extract numeric characters from the word
    return int(digits) if digits else float('inf')


print(order(sentence_to_sort))
print(order_sentence_by_digit(sentence_to_sort))
