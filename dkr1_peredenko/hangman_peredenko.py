# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters=''
    for i in secret_word:
        if i in letters_guessed:
            letters+=i
            if letters==secret_word:
                return True
        else:
            return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_letters=''
    for j in secret_word:
      if j in letters_guessed:
        guessed_letters+=j
      else:
        guessed_letters += '_ '
    return guessed_letters





def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available_letters_list=string.ascii_lowercase
    available_letters_list=list(available_letters_list)
    for k in letters_guessed:
      if k in available_letters_list:
        available_letters_list.remove(k)
    available_letters=''.join(available_letters_list)
    return available_letters

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses=6
    warnings=3
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ',len(secret_word),' letters long\n'
          '-------------')
    letters_guessed=[]
    vowels=['a', 'e', 'i', 'o', 'u']
    print('You have ', guesses, ' guesses left')
    print('Available letters:', get_available_letters(letters_guessed))
    while True:
        input_letter=input('Please guess a letter: ').lower()
        #правильні дані (без попереджень)
        if len(input_letter)==1 and input_letter.isalpha():
            #випадок 1. літери немає в слові
            if input_letter not in list(secret_word):
                #літера голосна, -2 спроби
                if input_letter in vowels:
                    guesses-=2
                    print('Oops! That letter is not in my word.')
                    print('Please guess a letter: ', is_word_guessed(secret_word, letters_guessed))
                #літера приголосна, -1 спроба
                else:
                    guesses-=1
                    print('Oops! That letter is not in my word.')
                    print('Please guess a letter: ', is_word_guessed(secret_word, letters_guessed))
            #випадок 2. літеру ще не вибрали
            if input_letter in list(get_available_letters(letters_guessed)):
                letters_guessed.append(input_letter)
                print('Good guess: ', is_word_guessed(secret_word, letters_guessed))
            #випадок 3. всі введені літери є в слові
            if get_guessed_word(secret_word, letters_guessed)==True:
                print('Congratulations, you won!')
                score=len(secret_word)*guesses
                print('Your total score for this game is: ', score)
        #якщо введено не літеру або введено більше одного символу, -1 попередження
        if not input_letter.isalpha() or len(input_letter)!=1:
            if warnings!=0:
               warnings-=1
               print('Oops! That is not a valid letter.')
               print('You have ', warnings, ' warnings left')
            if warnings<=0:
                guesses-=1
        #якщо літеру введено повторно, -1 попередження 
        if input_letter not in list(get_available_letters(letters_guessed)):
            if warnings!=0:
               warnings-=1
               print('Oops! You\'ve already guessed that letter.')
               print('You have ', warnings, ' warnings left')
            if warnings<=0:
                guesses-=1
        #якщо не залишилося спроб
        if guesses<=0:
            print('Sorry, you ran out of guesses. The word was ', secret_word)
            break



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word=my_word.replace(' ','')
    my_word_list=list(my_word.replace(' ',''))
    if len(other_word) == len(my_word):
        for l in range(len(my_word)):
            if my_word[l]==other_word[l]:
                continue
            if my_word[l]=='_' and other_word[l] not in my_word_list:
                continue
            else:
                return False
        return True
    else:
        return False


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    matches=''
    for word1 in wordlist:
        if match_with_gaps(my_word, word1):
            matches+=word1
    if matches!='':
        print('Possible matches: ', matches)
    if matches=='':
        print('No matches found')




def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses=6
    warnings=3
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ',len(secret_word),' letters long\n'
          '-------------')
    letters_guessed=[]
    vowels=['a', 'e', 'i', 'o', 'u']
    print('You have ', guesses, ' guesses left')
    print('Available letters:', get_available_letters(letters_guessed))
    while True:
        input_letter=input('Please guess a letter: ').lower()
        #правильні дані (без попереджень)
        if len(input_letter)==1 and input_letter.isalpha():
            if input_letter == '*':
                show_possible_matches(is_word_guessed(secret_word, letters_guessed))
                continue
            #випадок 1. літери немає в слові
            if input_letter not in list(secret_word):
                #літера голосна, -2 спроби
                if input_letter in vowels:
                    guesses-=2
                    print('Oops! That letter is not in my word.')
                    print('Please guess a letter: ', is_word_guessed(secret_word, letters_guessed))
                #літера приголосна, -1 спроба
                else:
                    guesses-=1
                    print('Oops! That letter is not in my word.')
                    print('Please guess a letter: ', is_word_guessed(secret_word, letters_guessed))
            #випадок 2. літеру ще не вибрали
            if input_letter in list(get_available_letters(letters_guessed)):
                letters_guessed.append(input_letter)
                print('Good guess: ', is_word_guessed(secret_word, letters_guessed))
            #випадок 3. всі введені літери є в слові
            if get_guessed_word(secret_word, letters_guessed)==True:
                print('Congratulations, you won!')
                score=len(secret_word)*guesses
                print('Your total score for this game is: ', score)
        #якщо введено не літеру або введено більше одного символу або не *, -1 попередження
        if (not input_letter.isalpha() and input_letter!='*') or len(input_letter)!=1:
            if warnings!=0:
               warnings-=1
               print('Oops! That is not a valid letter.')
               print('You have ', warnings, ' warnings left')
            if warnings<=0:
                guesses-=1
        #якщо літеру введено повторно, -1 попередження 
        if input_letter not in list(get_available_letters(letters_guessed)) and input_letter!='*':
            if warnings!=0:
               warnings-=1
               print('Oops! You\'ve already guessed that letter.')
               print('You have ', warnings, ' warnings left')
            if warnings<=0:
                guesses-=1
        #якщо не залишилося спроб
        if guesses<=0:
            print('Sorry, you ran out of guesses. The word was ', secret_word)
            break



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
