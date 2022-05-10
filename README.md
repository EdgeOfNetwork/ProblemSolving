# ProblemSolving

## BOJ (Python)  
출처 : https://ryute.tistory.com/33  
길라잡이,  

<hr/> 

### 1-1. 탐색과 정렬 (1)  
A – 1920 수 찾기 https://www.acmicpc.net/problem/1920 [V] 이진탐색  
B – 2750 수 정렬하기 https://www.acmicpc.net/problem/2750 [V] 퀵소트  
C – 2751 수 정렬하기 2 https://www.acmicpc.net/problem/2751 [V] 머지소트  

: 퀵을 사용했는데 메모리 초과나 오버플로가 자꾸 떴다.   
퀵의 최악의 경우인 O(N^2)가 나타났기 때문인 듯 하다.  
다른 답변들이 머지소트로 접근해서 일단은 써 봤는데 정답처리가 되었다.   
따라서 코테에서 sorting문제가 나오면 일단 merge를 쓰는게 맞는 듯 하다.   
  
D – 10989 수 정렬하기 3 https://www.acmicpc.net/problem/10989 [V] 카운팅소트  
  
: 2751에서 메모리 사용을 죽이는 방식이다. 다른 사람의 코드를 참고했는데  
와 풀이법 예술이었다.  방법을 기억했다가 두고두고 써먹어봐야겠다 
빈 리스트에 내용물을 채워넣고 이를 활용하는 방법이었다.  

찾아보니, 카운팅소트라는 이름이다.  다 각자 사용하는 방법이 다른 듯 하다.  
  
=> O(nlogn) O(logn) 구현  
  
E – 10815 숫자 카드 https://www.acmicpc.net/problem/10815  [V] 이진탐색  
  
문제를 풀기 전에 공부하기: 이진 탐색, O(nlgn) 정렬, 카운팅 정렬  
  
<hr/>

1-2. 기초 자료구조 (1)

A – 10828 스택 https://www.acmicpc.net/problem/10828 [V]  
B – 10845 큐 https://www.acmicpc.net/problem/10845 [V]  
C – 10866 덱 https://www.acmicpc.net/problem/10866  
D – 1406 에디터 https://www.acmicpc.net/problem/1406  


문제를 풀기 전에 공부하기: 스택, 큐, 덱, 연결 리스트

학습 유의사항: 역시 자료구조를 직접 구현하기보다는 std::stack, std::queue, std::deque, std::list를 활용하는 방향으로 학습해 보자.

<hr/>

1-3. 탐색과 정렬 (2)

A – 1026 보물 https://www.acmicpc.net/problem/1026

B – 1181 단어 정렬 https://www.acmicpc.net/problem/1181

C – 11650 좌표 정렬하기 https://www.acmicpc.net/problem/11650

C* - 11651 좌표 정렬하기 2 https://www.acmicpc.net/problem/11651

D – 10867 중복 빼고 정렬하기 https://www.acmicpc.net/problem/10867

E – 10816 숫자 카드 2 https://www.acmicpc.net/problem/10816

 

문제를 풀기 전에 공부하기: X

학습 유의사항: std::unique와 std::lower_bound와 std::upper_bound를 함께 활용해 개수를 구하는 테크닉은 매우 자주 등장한다. 또한 std::sort의 비교 함수 지정은 반드시 알아두어야 한다.

 

1-4. 기초 자료구조 (2)

A – 9012 괄호 https://www.acmicpc.net/problem/9012

B – 1874 스택 수열 https://www.acmicpc.net/problem/1874

C – 1158 조세퍼스 문제 https://www.acmicpc.net/problem/1158

D – 1966 프린터 큐 https://www.acmicpc.net/problem/1966

E – 5430 AC https://www.acmicpc.net/problem/5430

 

문제를 풀기 전에 공부하기: X

학습 유의사항: X

 

<SET 2>

 

2-1. 백트래킹 (1)

A – 6603 로또 https://www.acmicpc.net/problem/6603

B – 1182 부분집합의 합 https://www.acmicpc.net/problem/1182

C – 9095 1, 2, 3 더하기 https://www.acmicpc.net/problem/9095

D – 9663 N-Queen https://www.acmicpc.net/problem/9663

 

문제를 풀기 전에 공부하기: 백트래킹

학습 유의사항: X

 

2-2. 기초 수학 (1)

A – 1037 약수 https://www.acmicpc.net/problem/1037

B – 1978 소수 찾기 https://www.acmicpc.net/problem/1978

C – 1929 소수 구하기 https://www.acmicpc.net/problem/1929

D – 2609 최대공약수와 최소공배수 https://www.acmicpc.net/problem/2609

 

문제를 풀기 전에 공부하기: 에라토스테네스의 체, 유클리드 호제법

학습 유의사항: 최대한 효율적으로 구현할 수 있는 방법을 생각하며 구현해 보자.

 

2-3. 백트래킹 (2)

A – 14889 스타트와 링크 https://www.acmicpc.net/problem/14889

B – 15686 치킨 배달 https://www.acmicpc.net/problem/15686

C – 2661 좋은수열 https://www.acmicpc.net/problem/2661

D – 2580 스도쿠 https://www.acmicpc.net/problem/2580

 

문제를 풀기 전에 공부하기: X

학습 유의사항: X

 

2-4. 기초 수학 (2)

A – 2485 가로수 https://www.acmicpc.net/problem/2485

B – 1644 소수의 연속합 https://www.acmicpc.net/problem/1644

C – 6588 골드바흐의 추측 https://www.acmicpc.net/problem/6588

C* - 15711 환상의 짝꿍 https://www.acmicpc.net/problem/15711

D – 1016 제곱 ㄴㄴ 수 https://www.acmicpc.net/problem/1016

 

문제를 풀기 전에 공부하기: X

학습 유의사항: X

 <hr/>

<SET 3>

 
3-1. DFS와 BFS (1)

A – 1260 DFS와 BFS https://www.acmicpc.net/problem/1260 [V] 

B – 2667 단지번호붙이기 https://www.acmicpc.net/problem/2667 [V]  
  
문제를 잘 읽자    
sort() vs sorted,  
메서드를 쓸때는 docs를 읽자    
  
C – 1697 숨바꼭질 https://www.acmicpc.net/problem/1697 [V]  
  
D – 2178 미로 탐색 https://www.acmicpc.net/problem/2178 [ing]

E – 2606 바이러스 https://www.acmicpc.net/problem/2606

 
문제를 풀기 전에 공부하기: DFS와 BFS

학습 유의사항: X

 <hr/>

3-2. 기초 다이나믹 프로그래밍 (1)

A – 1003 피보나치 함수 https://www.acmicpc.net/problem/1003

B – 1463 1로 만들기 https://www.acmicpc.net/problem/1463

C – 2579 계단 오르기 https://www.acmicpc.net/problem/2579

D – 1932 정수 삼각형 https://www.acmicpc.net/problem/1932

E – 1149 RGB거리 https://www.acmicpc.net/problem/1149

 

문제를 풀기 전에 공부하기: 다이나믹 프로그래밍

학습 유의사항: 다이나믹 프로그래밍은 탑다운 방식과 바텀업 방식이 있다. 특정 문제는 둘 중 한 가지 방법으로만 풀리기도 하니, 둘의 장단점을 비교해서 두 방식으로 모두 문제를 해결할 수 있도록 하자.

 

3-3. DFS와 BFS (2)

A – 2206 벽 부수고 이동하기 https://www.acmicpc.net/problem/2206

B – 7576 토마토 https://www.acmicpc.net/problem/7576

B* – 7569 토마토 https://www.acmicpc.net/problem/7569

C – 9466 텀 프로젝트 https://www.acmicpc.net/problem/9466

D – 2636 치즈 https://www.acmicpc.net/problem/2636

E – 2583 영역 구하기 https://www.acmicpc.net/problem/2583

 

문제를 풀기 전에 공부하기: X

학습 유의사항: X

 

3-4. 기초 다이나믹 프로그래밍 (2)

A – 11726 2×n 타일링 https://www.acmicpc.net/problem/11726

A* - 11727 2×n 타일링 2 https://www.acmicpc.net/problem/11727

B – 1912 연속합 https://www.acmicpc.net/problem/1912

C – 2293 동전 https://www.acmicpc.net/problem/2293

D – 2156 포도주 시식 https://www.acmicpc.net/problem/2156

E – 11052 카드 구매하기 https://www.acmicpc.net/problem/11052

F – 11053 가장 긴 증가하는 부분 수열 https://www.acmicpc.net/problem/11053

문제를 풀기 전에 공부하기: X
학습 유의사항: X

<\hr>

<SET 4>

4-1. 그리디 알고리즘 (1)

A – 11047 동전 0 https://www.acmicpc.net/problem/11047 [V]  
B – 1931 회의실배정 https://www.acmicpc.net/problem/1931  
C – 2217 로프 https://www.acmicpc.net/problem/2217  
D – 2529 부등호 https://www.acmicpc.net/problem/2529  

문제를 풀기 전에 공부하기: 그리디 알고리즘

학습 유의사항: X

 

4-2. 파라메트릭 서치 (1)

A – 2805 나무 자르기 https://www.acmicpc.net/problem/2805

B – 1654 랜선 자르기 https://www.acmicpc.net/problem/1654

C – 2869 달팽이는 올라가고 싶다 https://www.acmicpc.net/problem/2869

D – 2512 예산 https://www.acmicpc.net/problem/2512

E – 2110 공유기 설치 https://www.acmicpc.net/problem/2110

 

문제를 풀기 전에 공부하기: 파라메트릭 서치

학습 유의사항: X

 

4-3. 힙

A – 1927 최소 힙 https://www.acmicpc.net/problem/1927

A* - 11279 최대 힙 https://www.acmicpc.net/problem/11279

B – 11286 절댓값 힙 https://www.acmicpc.net/problem/11286

C – 1715 카드 정렬하기 https://www.acmicpc.net/problem/1715

D – 1655 가운데를 말해요 https://www.acmicpc.net/problem/1655

 

문제를 풀기 전에 공부하기: 힙

학습 유의사항: std::priority_queue에서 최대 힙의 구현체를 제공한다. 우선순위 큐에 연산자를 추가로 넣는 방법을 반드시 알고 가자.

 

4-4. 그리디 알고리즘 (2)

A – 1202 보석 도둑 https://www.acmicpc.net/problem/1202

B – 9576 책 나눠주기 https://www.acmicpc.net/problem/9576

C - 13305 주유소 https://www.acmicpc.net/problem/13305

C* – 1826 연료 채우기 https://www.acmicpc.net/problem/1826

D – 1422 숫자의 신 https://www.acmicpc.net/problem/1422

 

문제를 풀기 전에 공부하기: X

학습 유의사항: X

 

SET 5~8

https://www.acmicpc.net/workbook/view/2419



<SET 5>

 

5-1. 파라메트릭 서치 (2)

A – 1939 중량제한 https://www.acmicpc.net/problem/1939

B – 2585 경비행기 https://www.acmicpc.net/problem/2585

C – 3079 입국심사 https://www.acmicpc.net/problem/3079

D – 3090 차이를 최소로 https://www.acmicpc.net/problem/3090

 

문제를 풀기 전에 공부하기: X

학습 유의사항: X

 

5-2. 다이나믹 프로그래밍 (1)

A – 1890 점프 https://www.acmicpc.net/problem/1890

B – 1520 내리막길 https://www.acmicpc.net/problem/1520

C – 12015 가장 긴 증가하는 부분 수열 2 https://www.acmicpc.net/problem/12015

D – 9251 LCS https://www.acmicpc.net/problem/9251

D* - 9252 LCS 2 https://www.acmicpc.net/problem/9252

E – 11051 이항 계수 2 https://www.acmicpc.net/problem/11051

 

문제를 풀기 전에 공부하기: X

학습 유의사항: X

 

5-3. 분할 정복 (1)

A - 1992 쿼드 트리 https://www.acmicpc.net/problem/1992

B – 11729 하노이 탑 이동 순서 https://www.acmicpc.net/problem/11729

C – 10827 a^b https://www.acmicpc.net/problem/10827

D – 2261 가장 가까운 두 점 https://www.acmicpc.net/problem/2261

 

문제를 풀기 전에 공부하기: 분할 정복

학습 유의사항: X

 

5-4. 유니온-파인드 트리 (1)

A – 1717 집합의 표현 https://www.acmicpc.net/problem/1717

B – 4195 친구 네트워크 https://www.acmicpc.net/problem/4195

C – 1976 여행 가자 https://www.acmicpc.net/problem/1976

D – 10775 공항 https://www.acmicpc.net/problem/10775

 

문제를 풀기 전에 공부하기: 유니온-파인드 트리

학습 유의사항: X

 

<SET 6>

 

6-1. 최단 경로 알고리즘 (1)

A – 1753 최단경로 https://www.acmicpc.net/problem/1753

A* - 1916 최소비용 구하기 https://www.acmicpc.net/problem/1916

B – 1238 파티 https://www.acmicpc.net/problem/1238

C – 1261 알고스팟 https://www.acmicpc.net/problem/1261

C* - 4485 녹색 옷 입은 애가 젤다지? https://www.acmicpc.net/problem/4485

D –1504 특정한 최단 경로 https://www.acmicpc.net/problem/1504

 

문제를 풀기 전에 공부하기: 다익스트라 알고리즘

학습 유의사항: X

 

6-2. 다이나믹 프로그래밍 (2)

 

A – 2618 경찰차 https://www.acmicpc.net/problem/2618

B – 1915 가장 큰 정사각형 https://www.acmicpc.net/problem/1915

C – 11066 파일 합치기 https://www.acmicpc.net/problem/11066

D – 2631 줄세우기 https://www.acmicpc.net/problem/2631

 

문제를 풀기 전에 공부하기: X

학습 유의사항: X

 

6-3. 최단 경로 알고리즘 (2)

A – 11657 타임머신 https://www.acmicpc.net/problem/11657

B – 11404 플로이드 https://www.acmicpc.net/problem/11404

C – 10159 저울 https://www.acmicpc.net/problem/10159

D – 1613 역사 https://www.acmicpc.net/problem/1613

 

문제를 풀기 전에 공부하기: 벨만-포드 알고리즘, 플로이드 알고리즘

학습 유의사항: X

 

6-4. 최소 스패닝 트리

A - 1197 최소 스패닝 트리 https://www.acmicpc.net/problem/1197

B – 1647 도시 분할 계획 https://www.acmicpc.net/problem/1647

C – 2887 행성 터널 https://www.acmicpc.net/problem/2887

 

문제를 풀기 전에 공부하기: 크루스칼 알고리즘, 프림 알고리즘

학습 유의사항: 크루스칼 알고리즘이 프림 알고리즘보다 비교적 자주 쓰인다. 두 알고리즘 모두 MST에 대한 핵심적인 통찰을 담고 있으니 정당성을 생각해 보며 문제를 풀어 보자.

 

<SET 7>

 

7-1. 위상 정렬

A – 2252 줄 세우기 https://www.acmicpc.net/problem/2252

B – 1005 ACM Craft https://www.acmicpc.net/problem/1005

C – 1766 문제집 https://www.acmicpc.net/problem/1766

D – 3665 최종 순위 https://www.acmicpc.net/problem/3665

 

문제를 풀기 전에 공부하기: 위상 정렬

학습 유의사항: X

 

7-2. 펜윅 트리와 세그먼트 트리 (1)

A - 2042 구간 합 구하기 https://www.acmicpc.net/problem/2042

B – 2357 최솟값과 최댓값 https://www.acmicpc.net/problem/2357

C – 7578 공장 https://www.acmicpc.net/problem/7578

D – 11505 구간 곱 구하기 https://www.acmicpc.net/problem/11505

 

문제를 풀기 전에 공부하기: 펜윅 트리, 세그먼트 트리

학습 유의사항: X

 

7-3. DFS와 BFS (3)

A – 1967 트리의 지름 https://www.acmicpc.net/problem/1967

B – 14867 물통 https://www.acmicpc.net/problem/14867

C – 1726 로봇 https://www.acmicpc.net/problem/1726

D – 6087 레이저 통신 https://www.acmicpc.net/problem/6087

 

문제를 풀기 전에 공부하기: X

학습 유의사항: X

 

7-4. 펜윅 트리와 세그먼트 트리 (2)

A – 3653 영화 수집 https://www.acmicpc.net/problem/3653

B – 2243 사탕상자 https://www.acmicpc.net/problem/2243

C – 5676 음주 코딩 https://www.acmicpc.net/problem/5676

D – 1849 순열 https://www.acmicpc.net/problem/1849

E – 2336 굉장한 학생 https://www.acmicpc.net/problem/2336

 

문제를 풀기 전에 공부하기: X

학습 유의사항: X

 

<SET 8>

 

8-1. 계산 기하 (1)

A – 11758 CCW https://www.acmicpc.net/problem/11758

B – 2166 다각형의 면적 https://www.acmicpc.net/problem/2166

C – 3679 단순 다각형 https://www.acmicpc.net/problem/3679

D – 6487 두 직선의 교차 여부 https://www.acmicpc.net/problem/6487

E – 1708 볼록 껍질 https://www.acmicpc.net/problem/1708

 

문제를 풀기 전에 공부하기: 기초적인 기하 알고리즘(CCW, 면적 구하기, 직선 교차 구하기 등), 볼록 껍질 구하는 알고리즘(Graham’s Scan, Andrew’s Algorithm)

학습 유의사항: X

 

8-2. 선형 자료구조의 활용

A – 2493 탑 https://www.acmicpc.net/problem/2493

B – 6198 옥상 정원 꾸미기 https://www.acmicpc.net/problem/6198

C – 6549 히스토그램에서 가장 큰 직사각형 https://www.acmicpc.net/problem/6549

D – 11003 최솟값 찾기 https://www.acmicpc.net/problem/11003

 

문제를 풀기 전에 공부하기: 슬라이딩 윈도우

학습 유의사항: X

 

8-3. 문자열 (1)

A – 1786 찾기 https://www.acmicpc.net/problem/1786

B – 1305 광고 https://www.acmicpc.net/problem/1305

C – 11656 접미사 배열 https://www.acmicpc.net/problem/11656

D – 5052 전화번호 목록 https://www.acmicpc.net/problem/5052

 

문제를 풀기 전에 공부하기: KMP 알고리즘, 접미사 배열

학습 유의사항: X

 

8-4. 다이나믹 프로그래밍 (3)

A – 2098 외판원 순회 https://www.acmicpc.net/problem/2098

B – 1102 발전소 https://www.acmicpc.net/problem/1102

C – 2718 타일 채우기 https://www.acmicpc.net/problem/2718

D – 1657 두부 장수 장홍준 https://www.acmicpc.net/problem/1657

 

문제를 풀기 전에 공부하기: 비트마스크

학습 유의사항: X



<SET 9>

 9-1. 유니온-파인드 트리 (2)

A - 2463 비용 https://www.acmicpc.net/problem/2463

B - 13306 트리 https://www.acmicpc.net/problem/13306

C - 15586 Mootube (Gold) https://www.acmicpc.net/problem/15586



문제를 풀기 전에 공부하기: X

학습 유의사항: X

 

9-2. 다이나믹 프로그래밍 (4)

A – 2449 전구 https://www.acmicpc.net/problem/2449

B – 16157 블로그 https://www.acmicpc.net/problem/16157

C – 2213 트리의 독립집합 https://www.acmicpc.net/problem/2213

D – 2330 기지국 https://www.acmicpc.net/problem/2300

 

문제를 풀기 전에 공부하기: X

학습 유의사항: X

 

9-3. 세그먼트 트리의 활용 (1)

A – 10999 구간 합 구하기 2 https://www.acmicpc.net/problem/10999

B – 1395 스위치 https://www.acmicpc.net/problem/1395

C – 12844 XOR https://www.acmicpc.net/problem/12844

D – 2820 자동차 공장 https://www.acmicpc.net/problem/2820

 

문제를 풀기 전에 공부하기: 레이지 프로파게이션

학습 유의사항: X

 

9-4. DFS 스패닝 트리의 활용 (1)

A – 11266 단절점 https://www.acmicpc.net/problem/11266

B – 11400 단절선 https://www.acmicpc.net/problem/11400

C – 2150 Strongly Connected Component https://www.acmicpc.net/problem/2150

D – 1199 오일러 회로 https://www.acmicpc.net/problem/1199



문제를 풀기 전에 공부하기: DFS 스패닝 트리, 타잔의 알고리즘, 코사라주의 알고리즘, 오일러 투어

학습 유의사항: 학습량이 많습니다. 타잔과 코사라주의 알고리즘의 차이점을 명확하게 비교하면서 학습합시다.





?-1. 계산 기하 (2)

B - 4181 Convex Hull https://www.acmicpc.net/problem/4181

C – 9240 로버트 후드 https://www.acmicpc.net/problem/9240

D – 13310 먼 별 https://www.acmicpc.net/problem/13310

E – 1688 지민이의 테러 https://www.acmicpc.net/problem/1688

 

문제를 풀기 전에 공부하기: 로테이팅 캘리퍼스, 포인트 인 폴리곤 테스트

학습 유의사항: X

 

?-2. 문자열 (2)

A – 5670 휴대폰 자판 https://www.acmicpc.net/problem/5670

B -9248 Suffix Array https://www.acmicpc.net/problem/9248

C - 9250 문자열 집합 판별 https://www.acmicpc.net/problem/9250

D – 1701 Cubeditor https://www.acmicpc.net/problem/1701

 

문제를 풀기 전에 공부하기: LCP 배열, 아호-코라식 알고리즘

학습 유의사항: X

 

X-1. DFS 스패닝 트리의 활용 (2)

A – 3682 동치 증명 https://www.acmicpc.net/problem/3682

B – 4013 ATM https://www.acmicpc.net/problem/4013

C – 11277 2-SAT – 3 https://www.acmicpc.net/problem/11280

C* - 11281 2-SAT – 4 https://www.acmicpc.net/problem/11281

D – 16367 TV Show Game https://www.acmicpc.net/problem/16367



문제를 풀기 전에 공부하기: 2-SAT

학습 유의사항: X
