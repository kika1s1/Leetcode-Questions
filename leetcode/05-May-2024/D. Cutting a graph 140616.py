# Problem: D. Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

class UnionFind:
    def __init__(self, size):
        self.parent = {i:i for i in range(size)}
        self.size = {i:1 for i in range(size)}

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self,x,y):
        repx = self.find(x)
        repy = self.find(y)

        if repx != repy:
            if self.size[repx] > self.size[repy]:
                self.parent[repy] = repx
                self.size[repx] += self.size[repy]
            else:
                self.parent[repx] = repy
                self.size[repy] += self.size[repx]
    def is_connected(self,x,y):
        return self.find(x) == self.find(y)            
   
n,m,q = map(int,input().split())
store = UnionFind(n+1)

for edge in range(m):
    _,_ = map(int,input().split())

reversed_commands = []

for query in range(q):
    comand = input().split()
    node1 = int(comand[2])
    node2 = int(comand[1])

    reversed_commands.append((comand[0],node1,node2))

reversed_commands.reverse()
reversed_answer = [] 

for comand,node1,node2 in reversed_commands:
    if comand == 'ask':
        if store.is_connected(node1,node2):
            reversed_answer.append('YES')
        else:
            reversed_answer.append('NO')
    else:
        store.union(node1,node2)

reversed_answer.reverse()  

for answer in  reversed_answer:
    print(answer)        




   



