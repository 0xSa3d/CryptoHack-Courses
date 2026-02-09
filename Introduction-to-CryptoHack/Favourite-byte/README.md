## Favourite Byte

### Category
Introduction — XOR Cryptanalysis

### Challenge Summary
The provided ciphertext has been encrypted using XOR with a single unknown byte.  
The goal is to recover the original message by identifying the correct byte used as the key.

### Approach
- Decode the given hexadecimal string into its raw byte sequence.
- Assume the encryption used a single-byte XOR key.
- Test all possible byte values as candidate keys.
- Evaluate the resulting plaintext for readable or meaningful output.

### Key Concept
Single-byte XOR is vulnerable to exhaustive key search due to the small key space (256 possibilities).  
Recognizing patterns in decoded output allows recovery of the original message without prior knowledge of the key.