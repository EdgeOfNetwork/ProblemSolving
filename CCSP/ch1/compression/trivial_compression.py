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