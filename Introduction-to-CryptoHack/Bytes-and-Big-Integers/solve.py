from Crypto.Util.number import *

integer_value = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

decoded_bytes = long_to_bytes(integer_value)
decoded_text = decoded_bytes.decode()

print(decoded_text)