from Crypto.Util.number import *

key1_hex = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key1_bytes = bytes.fromhex(key1_hex)
key1_int = bytes_to_long(key1_bytes)

key2_xor_key1_hex = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
key2_xor_key1_bytes = bytes.fromhex(key2_xor_key1_hex)
key2_xor_key1_int = bytes_to_long(key2_xor_key1_bytes)

key2_int = key1_int ^ key2_xor_key1_int

key2_xor_key3_hex = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
key2_xor_key3_bytes = bytes.fromhex(key2_xor_key3_hex)
key2_xor_key3_int = bytes_to_long(key2_xor_key3_bytes)

key3_int = key2_int ^ key2_xor_key3_int

flag_xor_all_keys_hex = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
flag_xor_all_keys_bytes = bytes.fromhex(flag_xor_all_keys_hex)
flag_xor_all_keys_int = bytes_to_long(flag_xor_all_keys_bytes)

final_flag_int = key1_int ^ key2_int ^ key3_int ^ flag_xor_all_keys_int

final_flag_bytes = long_to_bytes(final_flag_int)
print(final_flag_bytes.decode())