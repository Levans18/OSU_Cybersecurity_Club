from Crypto.Cipher import AES


key = b"Secret_16ByteKey"
cipher = AES.new(key, AES.MODE_ECB)

# Output: b'\x0e\xd9?Z\xdf\xa5\x11,]\xa3\\ax\xe3\x19\xe0'
decrypted = cipher.decrypt(b'\x0e\xd9?Z\xdf\xa5\x11,]\xa3\\ax\xe3\x19\xe0')
print(decrypted)
