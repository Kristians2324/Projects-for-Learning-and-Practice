from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

def run_aes_example():
    # 1. THE KEY: 256-bit security (standard for top-secret data)
    key = AESGCM.generate_key(bit_length=256)
    aes_engine = AESGCM(key)

    # 2. THE MESSAGE: Must be converted to 'bytes' using .encode()
    secret_data = "Hello Max, this is my AES code!".encode()

    # 3. THE NONCE: A random 12-byte 'salt' so the encryption is different every time
    nonce = os.urandom(12)

    # 4. ENCRYPT: This turns the text into unreadable gibberish
    ciphertext = aes_engine.encrypt(nonce, secret_data, None)

    print(f"Encrypted result: {ciphertext.hex()}")

    # 5. DECRYPT: Using the same Key and Nonce to get the message back
    decrypted_data = aes_engine.decrypt(nonce, ciphertext, None)
    
    print(f"Decrypted message: {decrypted_data.decode()}")

if __name__ == "__main__":
    run_aes_example()