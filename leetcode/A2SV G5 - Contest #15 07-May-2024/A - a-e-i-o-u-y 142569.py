# Problem: A - a-e-i-o-u-y - https://codeforces.com/gym/522079/problem/A

vowel = { "a", "e", "i", "o", "u", "y"}
word = []
n = int(input())
s = input()
for i in s:
    if word and word[-1] in vowel and i in vowel:
        continue
    else:
        word.append(i)
print("".join(word))