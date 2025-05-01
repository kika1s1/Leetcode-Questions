# Problem: B - String Fusion - https://codeforces.com/gym/526229/problem/B

class Trienode:
    def __init__(self):
    	self.child= {}
    	self.cnt = 0
    
   	 
class Trie:
    def __init__(self):
        self.root=Trienode()
   	 
    def insert(self, word: str) -> None:
        cur = self.root
        
        for c in word:
            ind=ord(c)-ord("a")

            if ind  not in cur.child:
                cur.child[ind]=Trienode()
            
            cur=cur.child[ind]
            cur.cnt += 1
   	 
   	 
    def search(self, word: str) -> int:
   	 
        cur=self.root
        tot = 0
        for c in word:
            ind=ord(c)-ord("a")
            if ind not in cur.child:
                return tot
            
            cur=cur.child[ind]
            tot += cur.cnt * 2

        return tot

n = int(input())
s = [input() for i in range(n)]
trie = Trie()
for cur in s:
	trie.insert(cur)
total = sum([len(cur)*2*n for cur in s])
for cur in s:
	total -= trie.search(cur[::-1])
print(total)