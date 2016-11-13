def break_words(stuff):
 """This function will break up words for us."""
 words = stuff.split(' ')
 
def sort_words(words):
 """Sorts the words."""
 return sorted(words)
 
def print_first_word(word):
 """prints the first word after popping it off."""
 word = words.pop(0)
 print word
 
def print_last_word(words):
 """prints the last word after popping it off."""
 word = word.pop(-1)
 print word
 
def sort_sentence(sentence):
 """Take in a full sentence and returns the sorted words."""
 word = break_words(sentence)
 return sort_words(words)
 
def print_first_and_last(sentence):
 """Prints the first and last word of tne sentence."""
 words = break_words(sentence)
 print_first_word(words)
 print_last_word(words)
 
