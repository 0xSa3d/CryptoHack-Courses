plaintext = "label"
xor_key = 13
result = ""
for i in plaintext:
    result += chr(ord(i) ^ xor_key)

print("crypto{" + result + "}")