## Base64

### Category
Introduction — Encoding

### Challenge Summary
Base64 is an encoding scheme used to represent binary data as printable ASCII characters.  
The challenge provides data encoded as a hexadecimal string and requires converting it into Base64 format.

### Approach
- Recognize that the provided input is in hexadecimal representation.
- Decode the hex string to obtain the underlying byte sequence.
- Re-encode the resulting bytes using Base64.

### Key Concept
Base64 is commonly used to safely transmit binary data over text-based systems such as web protocols.  
Correctly identifying data representations and converting between formats (hex → bytes → Base64) is a fundamental skill when handling encoded or encrypted data.