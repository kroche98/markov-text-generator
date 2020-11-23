from collections import defaultdict
import random, time
import sys

random.seed() # seed random generator with current time

def process_file(filename):
    # read in the corpus file
    with open(filename) as file:
        input_text = file.read()

    # convert the file into a list of words
    text = input_text.split()

    # create a dictionary of lists
    # by default, new keys are initialized to an empty list
    lookup = defaultdict(list)

    # iterate through the text and index it
    for i in range(len(text) - 1):
        lookup[text[i]].append(text[i+1])
    
    return lookup

def generate_text(lookup, text_length):
    wordlist = list(lookup.keys())
    output = ""

    # pick a first word
    current_word = random.choice(wordlist)
    output += current_word
    output += " "

    # generate the rest
    for _ in range(1, text_length):
        candidates = lookup[current_word]
        if len(candidates) > 0:
            next_word = random.choice(candidates)
        # sometimes the last word in the corpus has no successor
        # in which case we just pick a random word from the corpus
        else:
            next_word = random.choice(wordlist)
        output += next_word
        output += " "
        current_word = next_word
    
    return output

def main(args):
    if len(args) != 2:
        print("Invalid number of arguments")
        return
    
    filename, text_length = args

    try:
        text_length = int(text_length)
    except:
        print("Text length must be an integer")
        return
    
    if text_length <= 0:
        print("Text length argument must be a positive integer")
        return

    try:
        lookup = process_file(filename)
    except FileNotFoundError:
        print("Specified file not found")
        return
    except:
        print("An error occurred processing the file")
        return

    try:
        output = generate_text(lookup, text_length)
        print(output)
        return
    except:
        print("An error occurred generating the text")
        return


if __name__ == "__main__":
    main(sys.argv[1:])
