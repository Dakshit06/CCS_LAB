def diffie_hellman_key_exchange():
    p = 23
    g = 5
    print(f"Public Parameters:")
    print(f"Prime (p): {p}")
    print(f"Generator (g): {g}")
    print("-" * 40)
    
    a = 6
    b = 15
    print(f"Alice's private key (a): {a}")
    print(f"Bob's private key (b): {b}")
    print("-" * 40)
    
    A = pow(g, a, p)
    B = pow(g, b, p)
    print(f"Alice's public key (A = g^a mod p): {A}")
    print(f"Bob's public key (B = g^b mod p): {B}")
    print("-" * 40)
    
    print("Alice and Bob exchange public keys...")
    print("-" * 40)
    
    alice_shared_secret = pow(B, a, p)
    bob_shared_secret = pow(A, b, p)
    
    print(f"Alice computes shared secret (B^a mod p): {alice_shared_secret}")
    print(f"Bob computes shared secret (A^b mod p): {bob_shared_secret}")
    print("-" * 40)
    
    if alice_shared_secret == bob_shared_secret:
        print("Success! Both parties have computed the same shared secret.")
        print(f"Shared secret: {alice_shared_secret}")
    else:
        print("Error: The computed shared secrets do not match.")
        
    print("-" * 40)
    print("Mathematical verification:")
    print(f"Alice: B^a mod p = {g}^({b}*{a}) mod {p} = {g}^{b*a} mod {p} = {pow(g, b*a, p)}")
    print(f"Bob  : A^b mod p = {g}^({a}*{b}) mod {p} = {g}^{a*b} mod {p} = {pow(g, a*b, p)}")
    

if __name__ == "__main__":
    diffie_hellman_key_exchange()