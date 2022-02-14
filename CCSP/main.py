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


"""
HW TODO :
1. 자신의 설계 기법을 사용하여 피보나치 수열의 항목 n을 구하는 또 다른 함수를 작성하라.
이 장의 피보나치 수열 코드와 비교하여 정확성과 성능을 평가하는 단위테스트도 작성하라.
[] 기존의 피보나치 연구 
[] unittest 찾아보기

2. 파이썬 int 타입을 사용하여 단순히 비트 문자열을 표현하는 방법을 살펴봤다.
일반적으로 일련의 비트로 사용할 수 있는 int 타입 래퍼 클래스를 작성하라
(순회가능 iterable해야 하며, __getitem__을 구현한다)

3. 하노이의 탑 문제에서 탑 수에 상관없이 작동하는 코드를 작성하라
[] 1번의 응용인가?

4. 일회용 암호를 사용하여 이미지를 암호화하고 복호화하라.
[] opencv나 img 관련 lib 활용해야하나?
[] 일회용 암호?
[] 암호화 / 복호화 관련

"""