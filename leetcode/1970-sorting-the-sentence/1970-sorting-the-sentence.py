class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str

        Runtime complexity: O(1) constant
        Memory complexity: O(len(s)) depends on length of string

        """
        output = ""
        sarray = s.split()

        # Loop through all 9 possible position words
        for i in range(1, 10):

            # Find ith position word in string
            for word in sarray:

                # Insert word to output string
                if word[-1] == str(i):
                    output += " " + word[:-1]

        return output.strip()




