from ch1.compression.trivial_compression import CompressedGene
from ch1.compression.unbreakable_encryption import *

def compress():
    from sys import getsizeof
    original: str = "TAGGCCCGGTATATAGCTACTAGATATGATAGGATAGGAGACCTAGATATAG" * 100
    print("original: {} byte".format(getsizeof(original)))
    compressed: CompressedGene = CompressedGene(original)
    print("comp: {} byte".format(getsizeof(compressed.bit_string)))
    print(compressed) #압축 해제
    print("is it the same string between original and decompressed results? {}".format(original == compressed.decompress()))

def unb_comp():
    key1, key2 = encrypt("One Time Pad!")
    result:str = decrypt(key1, key2)
    print(result)

if __name__ == '__main__':
    #compress()
    unb_comp()