from enum import IntEnum
from typing import Tuple, List

#유전자 내에서 특정 코돈을 찾는 문제

#Enum이란

#IntEnum 비교연산자 사용 가능

Nucleotide: IntEnum = IntEnum('Nucleotide',('A', 'C','G','T'))
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Codon]

gene_str: str = "ATCGTGTGAGACGTACTACTACTACTCATCTGATCAGTGTGTACT"

def string_to_gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s): #현재 위치 다음에 2개의 문자가 없으면 실행 X
            return gene
        #3개의 nucliotide에서 codon 초기화
        codon : Codon = (Nucleotide[s[i]], Nucleotide[s[i + 1]], Nucleotide[s[i+2]])
        gene.append(codon)
    return gene

my_gene: Gene = string_to_gene(gene_str)
print(my_gene)

def linear_contatins(gene: Gene, key_codon: Codon) -> bool: #선형검색
    for codon in gene:
        if codon == key_codon: # 진짜 말 그대로 무식하게 검색
            return True
    return False


acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
gat: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.T)
print(linear_contatins(my_gene, acg))
print(linear_contatins(my_gene, gat))

#binary search는 모든 요소를 선형검색보다 빠르게 검색하지만, 자료구조의 저장 순서를 미리 알고 있어야 한다.
#저장순서를 미리 알고 있어야한다?

def binary_contains(gene: Gene, key_codon: Codon) -> bool:
    low: int = 0
    high: int = len(gene) - 1
    while low <= high: #검색 공간(범위)이 있을 때까지 수행
        mid: int = (low+high) // 2
        if gene[mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
            high = mid - 1
        else:
            return True
    return False

# Q : typehinting은 pythonic한 코딩인가?

my_sorted_gene: Gene = sorted(my_gene)
print(binary_contains(my_sorted_gene, acg))
print(binary_contains(my_sorted_gene, gat))

#이진 검색용으로 내장 라이브러리 bisect란 것이 있다
