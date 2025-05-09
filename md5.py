import hashlib

def generate_md5_hash(input_string):
    # object
    md5_hash = hashlib.md5()

    # encode string with utf8
    md5_hash.update(input_string.encode('utf-8'))

    # get hex hash
    return md5_hash.hexdigest()

if __name__== "__main__":
    # input
    input_string = input("Enter a string to hash using MD5: ")
    
    # hash
    result = generate_md5_hash(input_string)

    # O/P
    print(f"MD5 Hash of '{input_string}': {result}")