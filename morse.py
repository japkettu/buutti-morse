import re

class Morse:
    """
    A conversion table for encoding.
    """
    alphabets = {'A': '.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',\
            'F':'..-.', 'G':'--.','H':'....', 'I':'..', 'J':'.---', 'K':'-.-',\
            'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.','Q':'--.-',\
            'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-','W':'.--',\
            'X':'-..-', 'Y':'-.--', 'Z':'--..', '-':'.-.-.-', '.':'--..--',\
            '?':'..--..', '?':'..--..', '@':'.--.-.', '1':'.----', '2':'..---',\
            '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...',\
            '8':'---..', '9':'----.', '0':'-----'}

    def __init__(self, string):

        self.string = string.upper()

        """
        Swap key-value pairs for decoding morse.
        self.morse = {'.-':'A', ...}
        """
        self.morse = dict((v,k) for k,v in self.alphabets.items())

    def badChars(self, string):
        """
        Remove whitespace and find all non-morse characters.
        """
        string = string.replace(' ', '')
        c = re.findall("[^.-]", string)

        if (c):
            print('Bad characters: {}'.format(c))
            raise MorseDecodeError


    def encode(self):
        """
        Encodes ascii string to morse code.
        """
        
        s = ''
        try:
            for c in self.string:
                m = self.alphabets.get(c)
                if m == None:
                    raise MorseEncodeError
                s += ' {}'.format(m)
            # Remove first whitespace
            return s.strip()

        except MorseEncodeError:
            print ("Could not encode character: {}".format(c))
            raise

    def decode(self):
        """
        Decodes morse code to text string.
        Morse code should be separated by whitespace.
        """
        self.badChars(self.string)
        s = '' 
        try:
            for c in self.string.split(' '):
                m = self.morse.get(c)
                if m == None:
                    raise MorseDecodeError
                s += m

            return s.strip()

        except MorseDecodeError:
            print ("Could not decode morse: {}".format(c))
            raise

class MorseEncodeError(Exception):
    pass
class MorseDecodeError(Exception):
    pass
