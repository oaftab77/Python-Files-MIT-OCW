import string

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

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story


class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words("words_encryption_decryption.txt")
        
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
        COPY = self.valid_words[:]
        return COPY

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        dict_final = {}
        
        n = 0
        for char in string.ascii_lowercase:
            dict_final[char] = string.ascii_lowercase[(n + shift) % 26]
            n += 1
        
        n = 0
        for char in string.ascii_uppercase:
            dict_final[char] = string.ascii_uppercase[(n + shift) % 26]
            n += 1
        return dict_final
        
    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shift_dict = self.build_shift_dict(shift)
        
        string_new = ""
        for char in self.message_text:
            if char in shift_dict.keys():
                string_new = string_new + shift_dict[char]
            else:
                string_new = string_new + char
        
        return string_new
        
        
class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text)
        self.shift = shift
        self.valid_words_copy = Message.get_valid_words(self)
        self.encryption_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)
        
        
    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        dict_copy = self.encryption_dict.copy()
        return dict_copy

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        encryption_copy = self.message_text_encrypted
        return encryption_copy
        
        

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.encryption_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self,shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)
        self.valid_words_copy = Message.get_valid_words(self)
        
    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        prev_maximum = 0
        total_valid_words = 0
        
        for possible_shift in range(1, 26):
            shifted_string = Message.apply_shift(self, possible_shift)
            list_of_words = shifted_string.split(" ")
            
            if prev_maximum < total_valid_words:
                prev_maximum = total_valid_words            
            
            total_valid_words = 0
            
            for word in list_of_words:
                test_word = ""
                for char in word.lower():
                    if char in string.ascii_lowercase:
                        test_word += char
                        #Forgot that words could have punctuation attached                
                if test_word in self.valid_words_copy:
                    total_valid_words += 1
            
            if total_valid_words >  prev_maximum:
                ideal_tuple = (possible_shift, Message.apply_shift(self, possible_shift))                    
        return ideal_tuple           
            

if __name__ == '__main__':

    #Example test case (PlaintextMessage)
    plaintext = PlaintextMessage('hello', 2)
    print("\n" + 'Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())

    plaintext = PlaintextMessage('abc EFG', 1)
    print("\n" + 'Expected Output: cde GHI')
    plaintext.change_shift(2)
    print('Actual Output:', plaintext.get_message_text_encrypted())

    plaintext = PlaintextMessage('XYZ hji', 27)
    print("\n" + 'Expected Output: YZA ikj')
    print('Actual Output:', plaintext.get_message_text_encrypted())

    #Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage('jgnnq')
    print("\n" + 'Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message())

    ciphertext = CiphertextMessage('J bn Cpc')
    print("\n" + 'Expected Output:', (25, 'I am Bob'))
    print('Actual Output:', ciphertext.decrypt_message())

    ciphertext = CiphertextMessage('omfe mdq rgz')
    print("\n" + 'Expected Output:', (14, 'cats are fun'))
    print('Actual Output:', ciphertext.decrypt_message())
    
    story_file = open("story.txt", "r")
    story = story_file.read()
    print("\n" + str(story))
    story_file.close
    
    encrypted_story = CiphertextMessage(story)
    decrypted_story = encrypted_story.decrypt_message()
    print("\n" + str(decrypted_story))