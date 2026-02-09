## You Either Know, XOR You Don't

### Category
Introduction — XOR Cryptanalysis

### Challenge Summary
A ciphertext is provided that has been encrypted using a repeating XOR key.  
The challenge hints that knowledge of the expected flag format can assist in recovering the original message.

### Approach
- Decode the hexadecimal ciphertext into raw bytes.
- Use the known plaintext prefix (flag format) to derive part of the XOR key.
- Assume the key repeats across the entire message.
- Apply the recovered key cyclically to decrypt the full ciphertext.

### Key Concept
Repeating-key XOR is vulnerable when any portion of the plaintext is known or predictable.  
Known plaintext can be used to recover the corresponding segment of the key, which can then be reused to decrypt the remaining data.