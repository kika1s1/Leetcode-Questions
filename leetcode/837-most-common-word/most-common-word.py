import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.subn("[.,!?;']", ' ', paragraph.lower())[0].split(' ')
        
        paragraph = list(filter(lambda x: x not in banned + [''], paragraph))
        
        return Counter(paragraph).most_common(1)[0][0]