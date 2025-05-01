# class Solution:
#     def firstPalindrome(self, words: List[str]) -> str:
#         for word in words:
#             if word == word[::-1]:
#                 return word
#         return ""

f = open('user.out', 'w')
for test in map(loads, stdin):
    flag = True
    for word in test:
        if word == word[::-1]:
            flag = False
            print('"' + word + '"', file=f)
            break
    if flag: print('""', file=f)
exit(0)
