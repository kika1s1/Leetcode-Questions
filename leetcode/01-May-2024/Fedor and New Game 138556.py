# Problem: Fedor and New Game - https://codeforces.com/contest/467/problem/B

n, m, k = map(int, input().split())
data = []
for i in range(m):
    data.append(int(input()))
fedor = int(input())
cnt = 0

for num in data:
    if (fedor ^ num).bit_count() <=k:
        cnt +=1
print(cnt)