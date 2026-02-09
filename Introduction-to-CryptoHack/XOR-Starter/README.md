## XOR Starter

### Category
Introduction — Bitwise Operations

### Challenge Summary
This challenge introduces the XOR bitwise operator, which outputs 1 when two bits differ and 0 when they are the same.  
A given string must be transformed by applying XOR between each character and a fixed integer value.

### Approach
- Treat each character in the input string as its corresponding numeric value.
- Apply the XOR operation with the specified integer to each character individually.
- Convert the resulting values back into characters to reconstruct the transformed string.

### Key Concept
XOR is a reversible operation commonly used in simple encryption schemes.  
Understanding how XOR operates on bytes and characters is essential for later challenges involving encryption, key reuse, and cryptanalysis.