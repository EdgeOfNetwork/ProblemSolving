"""

2. 파이썬 int 타입을 사용하여 단순히 비트 문자열을 표현하는 방법을 살펴봤다.
일반적으로 일련의 비트로 사용할 수 있는 int 타입 래퍼 클래스를 작성하라
(순회가능 iterable해야 하며, __getitem__을 구현한다)

"""
#from typing import Generator

from secrets import token_bytes #의사 난수 생성 lib
from typing import Tuple


class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene) #make private

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1
        for nucleotide in gene.upper():
            self.bit_string <<= 2 #왼쪽으로 2비트 시프트
            if nucleotide == "A":
                self.bit_string |= 0b00 #or 연산자다
            elif nucleotide == "C":
                self.bit_string |= 0b01
            elif nucleotide == "G":
                self.bit_string |= 0b10
            elif nucleotide == "T":
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid nucleotide: {}".format(nucleotide))

    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() -1, 2): #1로 시작하므로 1을 뺀다
            bits: int = self.bit_string >> i & 0b11 #마지막 2비트 추출
            if bits == 0b00: #A
                gene += "A"
            elif bits == 0b01: #C
                gene += "C"
            elif bits == 0b10: #G
                gene += "G"
            elif bits == 0b11: #T
                gene += "T"
            else:
                raise ValueError("Invalid bits: {}".format(bits))
        return gene[::-1] #문자열을 뒤집음

    def __str__(self) -> str:
        return self.decompress()

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


if __name__ == '__main__':
    from sys import getsizeof
    original: str = "TAGGCCCGGTATATAGCTACTAGATATGATAGGATAGGAGACCTAGATATAG" * 100
    print("original: {} byte".format(getsizeof(original)))
    compressed: CompressedGene = CompressedGene(original)
    print("comp: {} byte".format(getsizeof(compressed.bit_string)))
    print(compressed) #압축 해제
    print("is it the same string between original and decompressed results? {}".format(original == compressed.decompress()))
    key1, key2 = encrypt("One Time Pad!")
    result:str = decrypt(key1, key2)
    print(result)