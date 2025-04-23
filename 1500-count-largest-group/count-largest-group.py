class Solution:
    def countLargestGroup(self, n: int) -> int:
        def add_number(n):
            total = 0
            while n > 0:
                total +=(n%10)
                n //=10
            return total

        sum_map = defaultdict(list)

        for i in range(1,n+1):
            sum_map[i].append(i)
            # if add_number(i) !=i:
            sum_map[add_number(i)].append(i)
        list_map = sorted(sum_map.values(), key=lambda x:len(x), reverse=True)
        print(list_map)
        f = 1
        maxim = len(list_map[0])
        for i in range(1, len(list_map)):
            if maxim == len(list_map[i]):
                f +=1
            else:
                return f
        return f
        