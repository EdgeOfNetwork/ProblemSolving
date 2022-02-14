from ch1.compression.trivial_compression import CompressedGene


def compress():
    from sys import getsizeof
    original: str = "TAGGCCCGGTATATAGCTACTAGATATGATAGGATAGGAGACCTAGATATAG" * 100
    print("original: {} byte".format(getsizeof(original)))
    compressed: CompressedGene = CompressedGene(original)
    print("comp: {} byte".format(getsizeof(compressed.bit_string)))
    print(compressed) #압축 해제
    print("is it the same string between original and decompressed results? {}".format(original == compressed.decompress()))

if __name__ == '__main__':
    compress()