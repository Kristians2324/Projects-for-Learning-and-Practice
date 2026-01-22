def simple_caesar(text, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted_text = ""

    # Convert input to lowercase so we only need one alphabet string
    text = text.lower()

    for char in text:
        if char in alphabet:
            # 1. Find the current position (0-25)
            position = alphabet.find(char)
            
            # 2. Add the shift and wrap around using modulo (%)
            new_position = (position + shift) % 26
            
            # 3. Add the new letter to our result
            encrypted_text += alphabet[new_position]
        else:
            encrypted_text += char

    return encrypted_text

message = input("Enter message: ")
shift = int(input("Enter shift: "))

print("Encrypted:", simple_caesar(message, shift))