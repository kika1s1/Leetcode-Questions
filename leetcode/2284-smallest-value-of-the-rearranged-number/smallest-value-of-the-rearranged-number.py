class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        if num < 0:
            st = list(str(num)[1:])

            st.sort(reverse=True)
            return -1* int("".join(st))
        else:
            st = list(str(num))
            st.sort()
            i, j  = 0, len(st)-1
            while int(st[i]) == 0:
                i +=1
            st[0], st[i] = st[i], st[0]
            return int("".join(st))
