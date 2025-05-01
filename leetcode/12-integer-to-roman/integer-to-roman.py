class Solution:
    def intToRoman(self, num: int) -> str:
        ram_to_roman = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }
        numbers = [1,4,5,9,10,40,50,90, 100, 400, 500, 900,1000]
        ans = ""
        while num != 0:
            length = len(str(num))
            rem = num//(10**(length-1))
            print(rem)
            value = rem * 10**(length-1)
            print(value)
            num -= value
            i = len(numbers)-1
            while value !=0:
                if value in ram_to_roman:
                    ans +=ram_to_roman[value]
                    value =0
                elif  value >= numbers[i]:
                    ans +=ram_to_roman[numbers[i]]
                    value -= numbers[i]
                else:
                    i -=1
        return ans




