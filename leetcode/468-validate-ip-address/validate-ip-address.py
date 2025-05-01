class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        ipv4 = queryIP.split(".")
        isIPv4 = True
        if len(ipv4) != 4:
            isIPv4 = False
        if isIPv4:
            for digit in ipv4:
                if not digit.isdigit():
                    isIPv4 = False
                    break
                elif not (0 <= int(digit) <=255):
                    isIPv4 = False
                    break
                elif len(digit) > 1 and 10 ** (len(digit)-1) > int(digit):
                    isIPv4 = False
                    break
        ipv6 = queryIP.split(":")
        isIPv6 = True
        if len(ipv6) !=8:
            isIPv6 = False

        chars = {"A","B","C", "D", "E", "F",  "a", "b", "c", "d", "e", "f", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}

        if isIPv6:
            for segment in ipv6:
                if not (1 <= len(segment) <=4):
                    isIPv6 = False
                    break
                for char in segment:
                    if char not in chars:
                        isIPv6 = False
                        break
                if not isIPv6:
                    break
        if isIPv4:
            return "IPv4"
        elif isIPv6:
            return "IPv6"
        return "Neither"