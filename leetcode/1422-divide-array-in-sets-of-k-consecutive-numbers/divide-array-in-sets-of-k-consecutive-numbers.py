class Solution:
    def isPossibleDivide(self, hand: List[int], groupSize: int) -> bool:
        card_freq = Counter(hand)
        hand.sort()

        for card in hand:
            if card_freq[card]:
                for next in range(card,card+groupSize):
                    if card_freq[next] == 0 or next not in card_freq:
                        return False
                    card_freq[next] -= 1
        return True
                

            


        