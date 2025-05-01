class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hashSet = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0]
            local = local.replace(".", "")
            hashSet.add((local, domain))
        return len(hashSet)
        