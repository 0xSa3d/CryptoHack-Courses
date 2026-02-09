# CryptoHack Introduction — Technical Notes

## Data Representation

### ASCII
- ASCII represents characters using integers (0–127).
- Text is fundamentally stored as numeric values.
- Converting between integers and characters is essential before any analysis.

### Hexadecimal

- Hex encodes raw bytes using base-16 representation.
- Common in ciphertext because many bytes are non-printable.
- Conversion workflow:
  - Hex → Bytes → Text (if printable)

### Base64

- Used to safely transport binary data across text-based systems.
- 4 Base64 characters represent 3 bytes.
- Common in web protocols and encoded files.

---

## Working with Bytes

- Cryptographic algorithms operate on bytes, not strings.
- Required transformations:
  - Characters ↔ Bytes
  - Bytes ↔ Hex
  - Bytes ↔ Base64
  - Bytes ↔ Integers

Understanding byte-level representation prevents misinterpreting encoded data.

---

## Bytes and Large Integers

- Public key systems (e.g., RSA) operate on numbers.
- Messages must be converted:
  - Message → ASCII bytes → Hex → Integer
- Reversing the process recovers plaintext.

---

## XOR Fundamentals

### Definition

XOR returns:
- 1 if bits differ
- 0 if bits are the same

### Properties

- Commutative: A ⊕ B = B ⊕ A
- Associative
- Identity: A ⊕ 0 = A
- Self-inverse: A ⊕ A = 0

These properties allow reversing chained XOR operations.

---

## XOR Weaknesses

### Single-byte XOR

- Key space is small (256 possibilities).
- Can be brute-forced.

### Repeating-key XOR

- Key repeats across the message.
- Known plaintext (e.g., flag format) leaks key material.

---

## Analyst Mindset Developed

- Always identify encoding first.
- Convert data to raw bytes before analysis.
- Use XOR properties algebraically.
- Prefer reasoning over blind brute force when possible.