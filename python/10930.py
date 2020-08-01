import hashlib

if __name__ == "__main__":
    string = input()
    encoded_string = string.encode()
    hexdigest = hashlib.sha256(encoded_string).hexdigest()
    print(hexdigest)