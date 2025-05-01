class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel = "aeiouAEIOU"
        s_list = list(s)
        initial = 0
        end = len(s_list)-1
        while initial < end:
            if s_list[initial] in vowel:
                if s_list[end] in vowel:
                    temp = s_list[initial]
                    s_list[initial] = s_list[end]
                    s_list[end] = temp
                    initial += 1
                    end -= 1
                else:
                    end -= 1
            else:
                initial += 1

        return "".join(s_list)