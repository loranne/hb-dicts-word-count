# import sys library to get argv method
import sys

# define the function
def file_word_count(filename):
    """Takes in a text file and returns a dict containing each word in the text, 
    along with a count of how many times that word appears."""

    # empty dict that will contain word counts
    word_counts = {}

    # open the text file
    text_file = open(filename)

    # loop over each line in the text file
    for line in text_file:
        # in each line, loop over each word
        for word in line.split():
            # for each word key, get the count value of that key. Add +1 to count
            word_counts[word] = word_counts.get(word, 0) + 1

    # loop over dict, for both key and value
    for key, value in word_counts.items():
        # print each key value pair
        print(f"{key} {value}")    
    
    # returns our dict of words and counts
    return word_counts


filename = sys.argv[1]
file_word_count(filename)