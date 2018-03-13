# Filename:   
# Created by: George Marshall 
# Created: 
# Description: counts the most common words in shakespeares complete works.
import string

# start of main
def main():
    fhand = open('shakes.txt')
    counts = dict()
    for line in fhand:
        line = line.translate(string.punctuation)  #next lines strip extra stuff out and format properly.
        line = line.lower()
        line = line.replace('+',' ')
        words = line.split()

        for word in words:           # counts the words.
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1

    # Sort the dictionary by value
    lst = list()
    for key, val in counts.items():
        lst.append((val, key))

    lst.sort(reverse=True)  # sorts the list from Greatest to least.

    # print the list out.
    for key, val in lst[:100]:
        print(key, val)

# runs this file if it is main
if __name__ == "__main__":
    main()
    
    
    
    
