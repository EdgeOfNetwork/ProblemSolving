from secrets import token_bytes #의사 난수 생성 lib
from typing import Tuple

def random_key(length: int) -> int:
    #length 만큼 임의의 byte 생성.
    tb : bytes = token_bytes(length)
    #바이트를 비트 문자열로 변환 후 반환함
    return int.from_bytes(tb, "big")

def encrypt(original: str) -> Tuple[int, int]:
    original_bytes: bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes, "big")
    encrypted: int = original_key ^ dummy # XOR연산
    return dummy, encrypted

def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2 #XOR
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    return temp.decode()