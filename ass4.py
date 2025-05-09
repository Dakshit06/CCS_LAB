from Crypto.Cipher import AES, DES
from secrets import token_bytes


def AES_encrypt():
    key = token_bytes(16)
    data = input("enter the data ").encode()

    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext = cipher.encrypt(data)
    
    print("Ciphertext:", ciphertext)
    return key, nonce, ciphertext

def AES_decrypt(key, nonce, ciphertext):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    
    print("Plaintext:", plaintext.decode())

def DES_encrypt():
    key = token_bytes(8)
    data = input("enter the data ").encode()

    cipher = DES.new(key, DES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext = cipher.encrypt(data)
        
    print("Ciphertext:", ciphertext)
    return key, nonce, ciphertext

def DES_decrypt(key, nonce, ciphertext):
    cipher = DES.new(key, DES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    
    print("Plaintext:", plaintext.decode())


if __name__ == "__main__":
    print("AES Encryption/Decryption:")
    key, nonce, ciphertext = AES_encrypt()
    AES_decrypt(key, nonce, ciphertext)
    
    print("\nDES Encryption/Decryption:")
    key, nonce, ciphertext = DES_encrypt()
    DES_decrypt(key, nonce, ciphertext)
