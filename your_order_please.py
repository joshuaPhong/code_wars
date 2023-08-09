# sort a string
sentence_to_sort = "This7 will6 be5 the4 sentence3 we2 sort1"
list_of_words = []

list_of_words = {}


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







print(order(sentence_to_sort))
