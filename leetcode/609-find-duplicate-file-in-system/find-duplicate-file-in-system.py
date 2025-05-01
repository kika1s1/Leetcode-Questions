class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        # key_value = defaultdict(list)
        # for line in paths:
        #     path = []
        #     open = False
        #     keys = []
        #     nums = []
        #     for char in line:
        #         if char == "(":
        #             open = True
        #         if char !=" " and not open:
        #             if char.isdigit():
        #                 path.append("/"+char)
                        
        #             else:
        #                 path.append(char)
        #         if char == ")":
        #             open = False
        #             key_value["".join(keys)].append("".join(path))
        #             keys = []
        #             path  = []
        #         if open and char !="" and char != "(":
        #             keys.append(char)
        # print(list(key_value.values()))
        keys = defaultdict(list)
        result = set()
        for line in paths:
            line = line.split(" ")
            root = line[0]
            for file in line[1:]:
                file = file.split("(")
                rt = file[0]
                file_content = file[1][:-1]
                keys["".join(file_content)].append(root + "/" + rt)
# print(keys)
        ans = []
        for keys , values in keys.items():
            if len(values) > 1:
                ans.append(values)
        return ans


         