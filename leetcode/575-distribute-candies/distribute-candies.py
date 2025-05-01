class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
            candy_len = int(len(candyType)/2)
            unique_candy_len = len(set(candyType))
            return min(candy_len,unique_candy_len)