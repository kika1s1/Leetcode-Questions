class Solution(object):
    def myAtoi(self, s):

        negative = False
        s = s.strip()

        if len(s) == 0:
            return 0
        elif len(s) > 0:
            if s.startswith("-"):
                negative = True
                s = s[1:]
            elif s.startswith("+"):
                s = s[1:]
                


        chars = ["1", "2", "3", "4", "5",
                "6", "7", "8", "9", "0"]

        res = ""
        for i in s:
            if i in chars:
                res += i
            else:
                break
        if res == "":
            return 0
        else:
            if negative:
                result = -1 * int(res)
                if result < -2147483648:
                    return -2147483648
                else:
                    return result

            else:
                result = int(res)
                if result > 2147483647:
                    return 2147483647
                else:
                    return result