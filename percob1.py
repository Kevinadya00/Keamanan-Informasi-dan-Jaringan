def encrypt(plaintext, shift):
    result = ""
    for char in plaintext:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def decrypt(ciphertext, shift):
    return encrypt(ciphertext, -shift)

# Meminta input dari pengguna
plaintext = input("Masukkan plaintext: ")
shift_amount = int(input("Masukkan jumlah pergeseran (shift amount): "))

# Enkripsi dan Dekripsi
encrypted_text = encrypt(plaintext, shift_amount)
decrypted_text = decrypt(encrypted_text, shift_amount)

# Menampilkan hasil
print("\nPlaintext:", plaintext)
print("Encrypted:", encrypted_text)
print("Decrypted:", decrypted_text)

