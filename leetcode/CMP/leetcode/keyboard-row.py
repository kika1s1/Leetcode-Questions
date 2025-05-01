class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        return [w for w in words if any([set(w.lower()) <= e for 
                                         e in [set("qwertyuiop"),
                                               set("asdfghjkl"),
                                               set("zxcvbnm")]
                                        ])
               ]