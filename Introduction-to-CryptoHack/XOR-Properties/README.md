## XOR Properties

### Category
Introduction — Bitwise Operations

### Challenge Summary
This challenge explores the fundamental algebraic properties of the XOR operation and demonstrates how they can be used to reverse a sequence of XOR-based transformations applied to encrypted data.

Several intermediate values are provided where multiple unknown keys have been XORed together with the flag. The goal is to recover the original message by leveraging XOR properties.

### Approach
- Convert the provided hexadecimal values into byte representations.
- Use the commutative and associative properties of XOR to reorder operations.
- Apply the self-inverse property (A ⊕ A = 0) to cancel repeated terms.
- Recover intermediate keys step by step, then use them to isolate and retrieve the original message.

### Key Concept
XOR has predictable algebraic behavior:
- Order of operands does not affect the result.
- Grouping of operations does not affect the result.
- XOR with zero leaves a value unchanged.
- XORing a value with itself cancels it.

These properties allow chained XOR operations to be reversed, highlighting why repeated or exposed key material can weaken XOR-based encryption.