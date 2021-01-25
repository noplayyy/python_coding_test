# 거스름돈 page.87

n = 1260 # 금액
count = 0 # 동전 개수 변수

coin_types = [500, 100, 50, 10] # 큰 단위 화폐부터 차례대로 확인

for coin in coin_types:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)