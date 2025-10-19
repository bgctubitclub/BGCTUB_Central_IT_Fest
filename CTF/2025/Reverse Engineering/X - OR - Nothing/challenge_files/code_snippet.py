def xor_data(data, key):
    return bytes([b ^ key for b in data])

def encrypt():
    with open("flag.txt", "rb") as f:
        plaintext = f.read()
    encrypted = xor_data(plaintext, KEY)
    with open("flag.enc", "wb") as f:
        f.write(encrypted)
    print("[+] Encrypted flag saved as flag.enc")