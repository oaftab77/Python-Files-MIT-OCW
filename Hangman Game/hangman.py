# Hangman Game
# -----------------------------------

import random
import string

WORDLIST_FILENAME = "words_hangman.txt"


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
    print(len(wordlist), "words loaded.")
    return wordlist

wordlist = load_words()

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    tracker = True
    for char in secret_word:        
        if char not in letters_guessed:
            tracker = False
    return tracker


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    ''' 
    display = ""
    for char in secret_word:
        if char in letters_guessed:
            display = display + char
        else:
            display = display + "_ "
    return(display)

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters_list = string.ascii_lowercase
    
    for char in letters_guessed:
        if char in letters_list:
            index = letters_list.index(char)
            letters_list = letters_list[:index] + letters_list[index + 1:]        
    return letters_list

# =============================================================================
# wordlist = load_words()
# secret_word = choose_word(wordlist)
# =============================================================================
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
    print("Welcome to the game Hangman. \nI am thinking of a word that is", len(secret_word), " letters long." + "\n-------------")
    warnings_remaining = 3
    guesses_remaining = 6
    letters_guessed = []
    available_letters = string.ascii_lowercase
    display = "_ "*len(secret_word)

    print("You have", warnings_remaining, "warnings remaining")

    while guesses_remaining > 0:               
        print("You have", guesses_remaining, "guesses remaining")
        print("Available letters are", available_letters, end = "")
        
        user_guess = input("Please guess one lowercase letter: ")
        
        if str.isalpha(user_guess) == False:
            print("Please guess one lowercase LETTER next time. ", end = "")
            if warnings_remaining == 0:
                guesses_remaining -= 1
                print("No warnings remaining, so you lose a guess. You have", guesses_remaining, "guesses remaining.")
            else:
                warnings_remaining -= 1
                print("Warnings remaining:", warnings_remaining)
            print(display)
        elif len(user_guess) > 1:
            print("Please guess ONE lowercase letter next time. ", end = "")
            if warnings_remaining == 0:
                guesses_remaining -= 1
                print("No warnings remaining, so you lose a guess. You have", guesses_remaining, "guesses remaining.")
            else:
                warnings_remaining -= 1
                print("Warnings remaining:", warnings_remaining)
            print(display)
        elif user_guess in letters_guessed:
            print("Please guess one NEW lowercase letter next time. ", end = "")
            if warnings_remaining == 0:
                guesses_remaining -= 1
                print("No warnings remaining, so you lose a guess. You have", guesses_remaining, "guesses remaining.")
            else:
                warnings_remaining -= 1
                print("Warnings remaining:", warnings_remaining)
            print(display)
        else:
            if str.lower(user_guess) != user_guess:
                print("We accept uppercase letters but prefer lower case")
                user_guess = str.lower(user_guess)
                
            letters_guessed += user_guess
            display = get_guessed_word(secret_word, letters_guessed)
            available_letters = get_available_letters(letters_guessed)
    
            if user_guess in secret_word:
                print("Good guess:", display, )
            else:
                print("That letter is not in the word:", display)
            if user_guess not in secret_word and user_guess in ["a", "e", "i", "o", "u"]:
                guesses_remaining -= 2
            elif user_guess not in secret_word:
                guesses_remaining -= 1
        print("------------")
        if is_word_guessed(secret_word,letters_guessed) == True:
            print("You won!")
            break
    if guesses_remaining <= 0:
        print("You ran out of guesses. The word was", secret_word)
    else:
        list = []
        for char in secret_word:
            if char not in list:
                list += char
        score = guesses_remaining*len(list)
        print("Your score is:", score)

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

    keeper = False
    
    
    #generates my_word as a word without spaces
    for char in my_word:
        if char == " ":
            index = my_word.index(" ")    
            my_word = my_word[:index] + my_word[index + 1:]
    
    #list of letters in my_word
    list_of_letters = []
    for char in my_word:
        if char != "_":
            list_of_letters += char
    
    if len(my_word) != len(other_word):
        return False
    else:
        
        
        for char in my_word:                     
            index = my_word.index(char)
            if char != "_":
                for i in range(my_word.count(char)):
                    if char == other_word[index]:
                        keeper = True
                        index = my_word.find(char, index + 1)
                    else:
                        keeper = False
                        return False                
            else:
                if other_word[index] not in list_of_letters:
                    keeper = True
                else:
                    keeper = False
                    break
    return keeper
            
# =============================================================================
# my_word = "t_ _ t"
# other_word = "tabs"
# print(match_with_gaps(my_word, other_word))          
# =============================================================================
    
    



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    listofwords = ""
    for test_word in wordlist:
        if match_with_gaps(my_word, test_word) == True:
            listofwords = listofwords + test_word + " "
    if len(listofwords) == 0:
        listofwords = "No matches found."
    return listofwords
            
#print(show_possible_matches("a_ pl_ "))


#wordlist = load_words()
#Is loaded at line 35, no need to reload
secret_word = choose_word(wordlist)
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
    print("Welcome to the game Hangman. \nI am thinking of a word that is", len(secret_word), " letters long." + "\n-------------")
    warnings_remaining = 3
    guesses_remaining = 6
    letters_guessed = []
    available_letters = string.ascii_lowercase
    display = "_ "*len(secret_word)

    print("You have", warnings_remaining, "warnings remaining")

    while guesses_remaining > 0:               
        print("You have", guesses_remaining, "guesses remaining")
        print("Available letters are", available_letters, end = "")
        
        user_guess = input("Please guess one lowercase letter or * for hints: ")
        
        if user_guess == "*":
            print("Possible matches are:", show_possible_matches(secret_word))
        elif str.isalpha(user_guess) == False:
            print("Please guess one lowercase LETTER next time. ", end = "")
            if warnings_remaining == 0:
                guesses_remaining -= 1
                print("No warnings remaining, so you lose a guess. You have", guesses_remaining, "guesses remaining.")
            else:
                warnings_remaining -= 1
                print("Warnings remaining:", warnings_remaining)
            print(display)
        elif len(user_guess) > 1:
            print("Please guess ONE lowercase letter next time. ", end = "")
            if warnings_remaining == 0:
                guesses_remaining -= 1
                print("No warnings remaining, so you lose a guess. You have", guesses_remaining, "guesses remaining.")
            else:
                warnings_remaining -= 1
                print("Warnings remaining:", warnings_remaining)
            print(display)
        elif user_guess in letters_guessed:
            print("Please guess one NEW lowercase letter next time. ", end = "")
            if warnings_remaining == 0:
                guesses_remaining -= 1
                print("No warnings remaining, so you lose a guess. You have", guesses_remaining, "guesses remaining.")
            else:
                warnings_remaining -= 1
                print("Warnings remaining:", warnings_remaining)
            print(display)
        else:
            if str.lower(user_guess) != user_guess:
                print("We accept uppercase letters but prefer lower case")
                user_guess = str.lower(user_guess)
                
            letters_guessed += user_guess
            display = get_guessed_word(secret_word, letters_guessed)
            available_letters = get_available_letters(letters_guessed)
    
            if user_guess in secret_word:
                print("Good guess:", display, )
            else:
                print("That letter is not in the word:", display)
            if user_guess not in secret_word and user_guess in ["a", "e", "i", "o", "u"]:
                guesses_remaining -= 2
            elif user_guess not in secret_word:
                guesses_remaining -= 1
        print("------------")
        if is_word_guessed(secret_word,letters_guessed) == True:
            print("You won!")
            break
    if guesses_remaining <= 0:
        print("You ran out of guesses. The word was", secret_word)
    else:
        list = []
        for char in secret_word:
            if char not in list:
                list += char
        score = guesses_remaining*len(list)
        print("Your score is:", score)


hangman_with_hints(secret_word)


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


# =============================================================================
# if __name__ == "__main__":
#     # pass
# 
#     # To test part 2, comment out the pass line above and
#     # uncomment the following two lines.
#     
#     secret_word = choose_word(wordlist)
#     hangman(secret_word)
# =============================================================================

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
