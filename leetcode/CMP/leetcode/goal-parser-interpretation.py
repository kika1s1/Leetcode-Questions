class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        string = command
        for i in range(len(command)):
            string = string.replace("(al)", "al", 1)
            string = string.replace("()", "o", 1)
        return string
