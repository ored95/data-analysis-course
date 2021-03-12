#!/usr/bin/env python3
'''
Create function word_frequencies that gets a filename as a parameter and returns a dict 
with the word frequencies. In the dictionary the keys are the words and the corresponding 
values are the number of times that word occurred in the file specified by the function 
parameter. Read all the lines from the file and split the lines into words using the split() method. 
Further, remove punctuation from the ends of words using the strip("""!"#$%&'()*,-./:;?@[]_""") method call.
'''

def word_frequencies(filename='src/alice.txt'):
    dict = {}
    with open(filename, 'r') as f:
        for line in f:
            words = [w.strip("""!"#$%&'()*,-./:;?@[]_""") for w in line.split()]
            for word in words:
                if word in dict.keys():
                    dict[word] += 1
                else:
                    dict[word] = 1
    return dict

def main():
    pass

if __name__ == "__main__":
    main()
