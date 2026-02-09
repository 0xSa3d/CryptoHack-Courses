hex_ciphertext = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
cipher_bytes = bytes.fromhex(hex_ciphertext)

for xor_key in range(256):
    decoded_text = ""
    for byte_value in cipher_bytes:
        decoded_text += chr(byte_value ^ xor_key)

    if "crypto" in decoded_text:
        print(decoded_text)