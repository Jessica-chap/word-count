# put your code here.
#input/ouput
# define a function to take in a file
#open that file and assign to varaible
#empty dictionary
# loop over the entire file
#for each word looped over somehow create that as a key, generic to apply to any text
#store key in empty dictionary
#once we have a key, we need to keep track of how many times that key comes up in text
#updating the value of that key - if word in words found key +=


def get_word_counts(filename):
    word_counts = {}
    file_text = open(filename)
    
    for line in file_text:
        words = line.split()
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1
    file_text.close()
    return word_counts
    

result = get_word_counts("twain.txt")
print(result)