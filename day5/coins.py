coins = {10: 0, 5: 0, 2: 0, 1: 0}
amount = int(input())
for i in coins:
    coins[i] = amount // i
    amount=amount % i

for k, v in coins.items():
    print(f"{v} coins of Rs.{k}" ) 