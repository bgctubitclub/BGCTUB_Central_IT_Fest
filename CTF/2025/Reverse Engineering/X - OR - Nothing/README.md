# X - OR - Nothing

**Category:** Reverse Engineering  
**Difficulty:** Medium  
**Points:** 100  
**Author:** h4x0r3rr0r

## 📖 Description

My friend received a zip archive from a stranger. The file included two files: one is **flag.enc**, and the other is just a **Python snippet**. But he failed to get the flag!

We have given you the file, can you get the flag for him?

## 📥 Files

- `code_snippet.py` - Encryption script
- `flag.enc` - Encrypted flag file

## 🚩 Flag Format

`BGCTUB_ITC{s0me_t3xt_@5_fl4g}`

## 💡 Hints

1. Understand the XOR encryption algorithm in the Python script
2. XOR is reversible - XOR the encrypted data with the key again
3. The key might be brute-forceable (single byte key: 0-255)
4. Look for readable ASCII characters in the decrypted output

## 🎥 Video Walkthrough

🎥 [Watch on YouTube](https://www.youtube.com/watch?v=87WI3xE1L8k&t=702s)

## 🏷️ Tags

`cipher` `python` `encryption-reversal` `brute-force`
