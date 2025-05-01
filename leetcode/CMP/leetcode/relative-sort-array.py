class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        answer = []
        for i in arr2:
            for j in range(arr1.count(i)):
                answer.append(i)
        sort1 = sorted(arr1)
        for i in sort1:
            if not i in answer:
                total = sort1.count(i)
                for j in range(total):
                    answer.append(i)
        return answer