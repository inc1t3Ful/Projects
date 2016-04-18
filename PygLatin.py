####
#PygLatin
####
#Converts all input to pyglatin
#Completed by Anthony Lee
#from Unit3: "Conditionals and Control Flow" on Codecademy

#Declare variables
pyg = 'ay'

#prompt
original = raw_input('Enter a word:')

#Check input size and nonletter input
if len(original) > 0 and original.isalpha():

    word = original.lower()
    first = word[0]
    new_word = word + first + pyg

    #splice from word[0] to end of word
    new_word = new_word[1:len(new_word)]
    print new_word

else:
    print 'empty' #if there is no input
    
