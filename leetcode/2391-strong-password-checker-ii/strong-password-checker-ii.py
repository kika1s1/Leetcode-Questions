class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        prev = ""
        if len(password) <8:
            return False
        condition = [0]*5
        for char in password:
            if prev ==char:
                return False
            elif char.isalpha() and char.islower():
                condition[0] =1
            elif char.isalpha() and char.isupper():
                condition[1] = 1
            elif char.isdigit():
                condition[2] = 1
            elif char in "!@#$%^&*()-+":
                condition[3] =1
            prev = char
        condition[4] =1
        return sum(condition) == 5