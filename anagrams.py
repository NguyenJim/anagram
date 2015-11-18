"""
This program returns all possible anagrams for a given string of characters.

Based on code written by Sam Allen.
http://www.dotnetperls.com/anagram-python
"""

def __main__():
    word = raw_input('Find anagram for ')
    dictionary = create_dict('wordlist.txt')
    results = anagram(dictionary, word)
    print 'Anagrams for', word
    print results

# Create the key dict
def create_dict(path):
    # Open english dictionary
    key_dict = {}
    outfile = open(path, "r")
    for line in outfile:
            line = line.strip()
            key = sorted_line(line)

	    # Create keys using sorted string/associate word with key
            if key in key_dict:
                key_dict[key].append(line)
            else:
                key_dict[key] = [line]
    outfile.close()
    return key_dict

# Sort letters in string alphabetically
def sorted_line(line):
    sort = sorted(line)
    return ''.join(sort)

# Returns all anagrams using key
def anagram(dictionary, line):
    key = sorted_line(line)
    return dictionary.get(key)
    
__main__()
