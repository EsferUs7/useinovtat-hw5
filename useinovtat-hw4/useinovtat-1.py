class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def encode(self, text):
        encoded = ""
        for i in range(len(text)):
            if text[i] not in self.alphabet or self.key[i % len(self.key)] not in self.alphabet:
                encoded += text[i]
            else:
                ind = (self.alphabet.index(text[i]) + self.alphabet.index(self.key[i % len(self.key)])) % len(
                    self.alphabet)
                encoded += self.alphabet[ind]
        return encoded

    def decode(self, text):
        encoded = ""
        for i in range(len(text)):
            if text[i] not in self.alphabet or self.key[i % len(self.key)] not in self.alphabet:
                encoded += text[i]
            else:
                ind = (self.alphabet.index(text[i]) + len(self.alphabet) - self.alphabet.index(
                    self.key[i % len(self.key)])) % len(self.alphabet)
                encoded += self.alphabet[ind]
        return encoded
