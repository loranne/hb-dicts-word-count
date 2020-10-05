def file_word_count(filename):
    word_counts = {}

    text_file = open(filename)

    for line in text_file:
        for word in line.split():
            word_counts[word] = word_counts.get(word, 0) + 1

    for key, value in word_counts.items():
        print(f"{key} {value}")    
        




    #for word in text_file:
    #    word_counts[word] = word_counts.get(word, 0) + 1
    
    return word_counts

file_word_count("test.txt")


    