# Problem: A - Ascend - https://codeforces.com/gym/526229/problem/A

n = int(input())
data = list(map(int, input().split()))
cnt = 1
ans = 1
for i in range(len(data)-1):
    if data[i] < data[i+1]:
        cnt +=1
        ans = max(cnt, ans)
    else:
        cnt =1
print(ans)