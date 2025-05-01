class Solution:
    def nextGreaterElement(self, n: int) -> int:
        change = 0
        data = [x for x in str(n)]
        l, r = len(data)-2, len(data)-1
        while l >= 0 and l < r:
            if data[l] < data[r]:
                forward = sorted(data[r:])
                r = 0
                change = 1
                while r < len(forward):
                    if data[l] < forward[r]:
                        data[l], forward[r] = forward[r], data[l]
                        data = data[:l+1]+forward
                        break
                    r +=1
                break
            r -=1
            l -=1

        if change == 0:
            return -1
        else:
            ans = int("".join(data))
            if ans >2**31 - 1:
                return -1

            return ans
