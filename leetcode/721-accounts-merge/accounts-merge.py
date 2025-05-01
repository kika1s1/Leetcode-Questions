class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = [i for i in range(n)]
        
        def find(n):
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        
        def union(u, v):
            p1, p2 = find(u), find(v)
            if p1 == p2:
                return True
            parent[p1] = p2
            return False
        
        seen = defaultdict()
        
        for i, account in enumerate(accounts):
            emails = account[1:]
            for email in emails:
                if email not in seen:
                    seen[email] = i
                else:
                    union(i, seen[email])
        
        all_emails = defaultdict(set)
        for email, i in seen.items():
            all_emails[find(i)].add(email)
        
        res = []
        
        for index, emails in all_emails.items():
            res.append([accounts[index][0]] + sorted(emails))
        
        return res