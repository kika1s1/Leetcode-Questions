class MagicDictionary:
    def __init__(self):
        self.words = []
    def buildDict(self, dictionary: List[str]) -> None:
        self.words.extend(dictionary)
    def search(self, searchWord: str) -> bool:
        for word in self.words:
            cnt = 0
            if len(word) == len(searchWord):
                for a, b in zip(word, searchWord):
                    if a !=b:
                        cnt +=1
                if cnt == 1:
                    return True
        return False

        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)