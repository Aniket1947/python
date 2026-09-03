import random
import string

def encoding(msg):
    words = msg.split(" ")
    new = []
    for word in words:
        if len(word) >= 3:
            new_st = word[1:] + word[0]
            random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=3))
            new.append(random_chars + new_st + random_chars)
        else:
            new.append(word[::-1])
    new_msg = " ".join(new)
    print(f"Encoded message: {new_msg}")
    return new_msg


def decoding(encoded_msg):
    words = encoded_msg.split(" ")
    decoded = []
    for word in words:
        if len(word) >= 9: 
            word = word[3:-3]
            decoded.append(word[-1] + word[:-1])
        else:
            decoded.append(word[::-1])
    decoded_msg = " ".join(decoded)
    print(f"Decoded message: {decoded_msg}")
    return decoded_msg


msg = input("Enter your message: ")
encoded = encoding(msg)
decoding(encoded)
