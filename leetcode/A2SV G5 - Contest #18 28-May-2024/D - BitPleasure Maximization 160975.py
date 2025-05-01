# Problem: D - BitPleasure Maximization - https://codeforces.com/gym/526229/problem/D


class TrieNode:
    def __init__(self):
        self.ind = None
        self.children = [None for _ in range(2)]


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, i):
        cur = self.root
        for ch in range(len(word)):
            order = int(word[ch])
            if not cur.children[order]:
                cur.children[order] = TrieNode()
            cur = cur.children[order]
        cur.ind = i

    def search(self, word):
        cur = self.root
        for ch in range(len(word)):
            order = abs(int(word[ch])-1)
            order1 = int(word[ch])
            if not cur.children[order]:
                if cur.ind:
                    return cur.ind
                else:
                    cur = cur.children[order1]
                    continue
            cur = cur.children[order]
        return cur.ind


n = int(input())

arr = [int(i) for i in input().split()]

prefix = [arr[0]]
postfix = [arr[-1]]

for i in range(1, n):
    prefix.append(prefix[-1] ^ arr[i])
for j in range(n-2, -1, -1):
    postfix.append(postfix[-1] ^ arr[j])
trie = Trie()
maxiPo = max(postfix).bit_length()
maxiPr = max(prefix).bit_length()
maxi = max(maxiPo, maxiPr)
for i, val in enumerate(postfix):
    b = bin(val)[2:]
    l = len(b)
    trie.insert((maxi-l)*"0"+b, i)
ans = max(prefix[0], postfix[0], prefix[-1], postfix[-1])
for i in range(len(prefix)-1):
    b = bin(prefix[i])[2:]
    l = prefix[i].bit_length()
    index = trie.search((maxi-l)*"0"+b)
    ans = max(ans, prefix[i] ^ postfix[index])
prefix.append(ans)
print(max(prefix+postfix))
