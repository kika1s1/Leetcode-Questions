class ATM:
    bank, val = [0] * 5, [20, 50, 100, 200, 500]
    
    def deposit(self, banknotesCount: List[int]) -> None:
        self.bank = [a + b for a, b in zip(self.bank, banknotesCount)]
    
    def withdraw(self, amount: int) -> List[int]:
        take = [0] * 5
        for i in range(4, -1, -1):
            take[i] = min(self.bank[i], amount // self.val[i])
            amount -= take[i] * self.val[i]
        if amount == 0:
            self.bank = [a - b for a, b in zip(self.bank, take)]
        return [-1] if amount else take

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)