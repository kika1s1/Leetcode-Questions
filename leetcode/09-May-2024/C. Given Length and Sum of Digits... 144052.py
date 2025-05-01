# Problem: C. Given Length and Sum of Digits... - https://codeforces.com/contest/489/problem/C

m, s = map(int, input().split())

if s == 0:
    if m == 1:
        print(0, 0)
    else:
        print(-1, -1)
else:
    if s > 9 * m or s == 0:
        print(-1, -1)
    else:
        maxim = [0 for _ in range(m)]
        minim = [0 for _ in range(m)]
        s_temp = s

        for i in range(m):
            if s_temp >= 9:
                maxim[i] = 9
                s_temp -= 9
            else:
                maxim[i] = s_temp
                s_temp = 0
                break

        minim[0] = 1
        s_temp = s - 1

        for i in range(m - 1, 0, -1):
            if s_temp >= 9:
                minim[i] = 9
                s_temp -= 9
            else:
                minim[i] = s_temp
                s_temp = 0
                break

        minim[0] += s_temp

        print("".join(map(str, minim)), "".join(map(str, maxim)))