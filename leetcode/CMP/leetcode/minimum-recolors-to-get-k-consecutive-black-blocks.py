class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        #tamirat
        minam = float("inf")
        for i in range(len(blocks)-(k-1)):
            sub = blocks[i:k+i]
            minam = min(sub.count("W"), minam)
        return minam


            