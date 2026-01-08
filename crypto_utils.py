import hashlib
import os

# Phase 1: Salting
def add_salt(password: str, salt: bytes) -> bytes:
    return password.encode() + salt

# Phase 2: MD5 hashing
def generate_key(password: str, salt: bytes) -> bytes:
    salted_password = add_salt(password, salt)
    return hashlib.md5(salted_password).digest()

# Text → Binary
def text_to_binary(text: str) -> str:
    return ''.join(format(ord(c), '08b') for c in text)

# Binary → Text
def binary_to_text(binary: str) -> str:
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(c, 2)) for c in chars)

# XOR Encryption / Decryption
def xor_process(binary: str, key: bytes) -> str:
    key_bits = ''.join(format(b, '08b') for b in key)
    return ''.join(
        str(int(binary[i]) ^ int(key_bits[i % len(key_bits)]))
        for i in range(len(binary))
    )
