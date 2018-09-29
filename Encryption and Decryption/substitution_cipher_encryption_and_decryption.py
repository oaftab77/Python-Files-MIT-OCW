import string
from recursive_permutation_function import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    #print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    #print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words_encryption_decryption.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        COPY = self.valid_words
        return COPY
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        vowels_permutation_lower = vowels_permutation.lower()
        vowels_permutation_upper = vowels_permutation.upper()
        
        dict_final = {}
        n = 0
        i = 0
        for char in string.ascii_letters:
            if char in vowels_permutation_lower:
                dict_final[char] = vowels_permutation_lower[n]
                n += 1
            elif char in vowels_permutation_upper:
                dict_final[char] = vowels_permutation_upper[i]
                i += 1
            else:
                dict_final[char] = char
        
        return dict_final
            
        
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        string_new = ""
        for char in self.message_text:
            if char in transpose_dict:
                string_new += transpose_dict[char]
            else:
                string_new += char        
        return string_new
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self,text)
        self.valid_words_copy = SubMessage.get_valid_words(self)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        vowels = "aeiou"
        
        correct_string = ""
        
        prev_max = 0
        total_valid_words = 0
        
        
        for elem in get_permutations(vowels):
            transpose_dict = SubMessage.build_transpose_dict(self, elem)
            
            decrypted_string = ""
            for char in self.message_text:
                if char in transpose_dict:
                    decrypted_string += transpose_dict[char]
                else:
                    decrypted_string += char
                    
            split_string = decrypted_string.split()
            
            if prev_max < total_valid_words:
                prev_max = total_valid_words 
            total_valid_words = 0 #forgot to reinitalize        
            
            for word in split_string:
                
                test_word = ""
                for char in word.lower():
                    if char in string.ascii_lowercase:
                        test_word += char
                        #Forgot that words could have punctuation attached

                if test_word in self.valid_words_copy: #forgot to make words lowercase
                    total_valid_words += 1
                        
            if total_valid_words > prev_max:
                correct_string = decrypted_string
            
            
        return correct_string
                
    

if __name__ == '__main__':


    message = SubMessage("Hello!")
    permutation = "eaiuo"
    dictionary = message.build_transpose_dict(permutation)
    
    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("\nOriginal message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
    
    message = SubMessage("~!@#@!All my ants are EIOU!")
    permutation = "uoiea"
    enc_dict = message.build_transpose_dict(permutation)
    print("\nOriginal message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "~!@#@!Ull my unts uro OIEA!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    
    enc_message = EncryptedSubMessage("~!@#@!Ull my unts uro OIEA!")
    permutation = "uoiea"
    enc_dict = message.build_transpose_dict(permutation)
    print("\nOriginal message:", enc_message.get_message_text(), "Permutation:", permutation)
    print("Expected decryption:", "~!@#@!All my ants are EIOU!")
    print("Actual decryption:", enc_message.decrypt_message())
    
    message = SubMessage("this is a sentence!")
    permutation = "aeiou"
    enc_dict = message.build_transpose_dict(permutation)
    print("\nOriginal message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "this is a sentence!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    
    enc_message = EncryptedSubMessage("this is a sentence!")
    permutation = "aeiou"
    enc_dict = message.build_transpose_dict(permutation)
    print("\nOriginal message:", enc_message.get_message_text(), "Permutation:", permutation)
    print("Expected decryption:", "this is a sentence!")
    print("Actual decryption:", enc_message.decrypt_message())
    