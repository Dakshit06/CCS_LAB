#RSA Algorithm Implementation
import random
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x1, y1 = extended_gcd(b % a, a)
            x = y1 - (b // a) * x1
            y = x1
            return gcd, x, y
    
    g, x, y = extended_gcd(e, phi)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % phi

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    
    d = mod_inverse(e, phi)
    
    return ((e, n), (d, n), phi)

def encrypt(public_key, message):
    e, n = public_key
    return pow(message, e, n)

def decrypt(private_key, ciphertext):
    d, n = private_key
    return pow(ciphertext, d, n)

def main():
    print("RSA Algorithm Implementation")
    print("-" * 40)
    
    while True:
        p = int(input("Enter a prime number (p): "))
        if is_prime(p):
            break
        print("Number must be prime. Try again.")
    
    while True:
        q = int(input("Enter a different prime number (q): "))
        if is_prime(q) and p != q:
            break
        print("Number must be prime and different from p. Try again.")
    
    public_key, private_key, phi = generate_keypair(p, q)
    e, n = public_key
    d, _ = private_key
    
    print("-" * 40)
    print(f"n = p*q = {n}")
    print(f"phi(n) = {phi}")
    print(f"Public key (e, n): ({e}, {n})")
    print(f"Private key (d, n): ({d}, {n})")
    print("-" * 40)
    
    max_message = n - 1
    print(f"Note: Message must be an integer between 1 and {max_message}")
    
    while True:
        message = int(input("Enter message to encrypt: "))
        if 0 < message < n:
            break
        print(f"Message must be between 1 and {n-1}. Try again.")
    
    ciphertext = encrypt(public_key, message)
    print(f"Encrypted message: {ciphertext}")
    
    decrypted_message = decrypt(private_key, ciphertext)
    print(f"Decrypted message: {decrypted_message}")
    
    if message == decrypted_message:
        print("Verification successful!")
    else:
        print("Verification failed!")

if __name__ == "__main__":
    main()