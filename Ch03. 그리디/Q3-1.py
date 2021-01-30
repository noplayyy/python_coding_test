# 숫자 카드 게임 page.96
# min() 함수를 이용하는 답안 예시

n, m = map (int, input().split()) # N, M을 공백으로 구분하여 입력받기

result = 0

# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data) # 현재 줄에서 '기징 직은 수' 찾기 
    result = max(result, min_value) # '가장 작은 수'들 중에서 가장 큰 수 찾기

print(result) # 최종 답안 출력