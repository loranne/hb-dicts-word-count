import sys

def file_word_count(filename):
    word_counts = {}

    text_file = open(filename)

    for line in text_file:
        for word in line.split():
            word_counts[word] = word_counts.get(word, 0) + 1

    for key, value in word_counts.items():
        print(f"{key} {value}")    
    
    return word_counts

file_word_count(argv[1])

