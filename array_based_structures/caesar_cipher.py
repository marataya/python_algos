class CaesarCipher:
    def __init__(self, shift):
        encoder = [None] * 26
        decoder = [None] * 26
        for k in range(26):
            encoder[k] = chr(ord('A') + (k + shift) % 26)
            decoder[k] = chr(ord('A') + (k - shift) % 26)
        self._encoder = ''.join(encoder)
        self._decoder = ''.join(decoder)

    def encrypt(self, msg):
        return self._transform(msg, self._encoder)

    def decrypt(self, msg):
        return self._transform(msg, self._decoder)

    def _transform(self, original, code):
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]
        return ''.join(msg)

if __name__ == '__main__':
    cipher = CaesarCipher(5)
    msg = 'DO NOT ADVANCE'
    encoded = cipher.encrypt(msg)
    print(encoded)
    decoded = cipher.decrypt(encoded)
    print(decoded)

