# Problem: A - Distribute - https://codeforces.com/gym/524965/problem/A

n = int(input())
data = list(map(int, input().split()))
total = sum(data)
pos  = total//(n//2)
for i in range(n):
    for j in range(n):
        if i !=j:
            if data[i] + data[j] == pos:
                print(i+1,j+1)
                data[i] = float("inf")
                data[j] = float("inf")
