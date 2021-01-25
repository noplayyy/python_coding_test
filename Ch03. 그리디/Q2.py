# 큰 수의 법칙  page.92

n, m, k= map(int, input().split()) # N, M, K를 공백으로 구분해 입력

data = list(map(int, input().split())) # N개의 수를 공백을 구분해 입력

data.sort() # 입력 받은 수 정렬

first = data[n-1] # 가장 큰 수
second = data[n-2] # 두 번째로 큰 수

result = 0 # 결과 변수

while True:
    for i in range(k): # 가장 큰 수를 K번 더하기
        if m == 0: # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1 # 더할 때마다 1씩 빼기
    if m == 0: # m이 0이라면 반복문 탈출
        break
    result += second # 두번째로 큰 수를 한 번 더하기
    m -= 1 # 더할 때마다 1씩 빼기

print(result)