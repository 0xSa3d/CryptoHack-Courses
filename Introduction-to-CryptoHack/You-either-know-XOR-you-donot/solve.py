cipher_hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
cipher_bytes = bytes.fromhex(cipher_hex)

known_flag_prefix = b"crypto{"

recovered_key_part = ""
for i in range(len(known_flag_prefix)):
    recovered_key_part += chr(known_flag_prefix[i] ^ cipher_bytes[i])

print(recovered_key_part)

# we found key (myXORke)
# by guessing, it will be (myXORkey)

full_xor_key = b"myXORkey"

decrypted_text = ""
for i in range(len(cipher_bytes)):
    decrypted_text += chr(cipher_bytes[i] ^ full_xor_key[i % len(full_xor_key)])

print(decrypted_text)