class Bank:

    def __init__(self, balance: List[int]):
        self.accountNumber = balance
        self.length = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if (account1-1 > self.length-1 or account2 - 1 >self.length-1) or (account1-1 <0 or account2 -1 < 0):
            return False
        if self.accountNumber[account1-1] < money:
            return False
        self.accountNumber[account1-1] -= money

        self.accountNumber[account2-1] +=money
        return True


    def deposit(self, account: int, money: int) -> bool:
        if account-1 > self.length-1 or account <=0:
            return False
        self.accountNumber[account-1] +=money
        return True
        
        

    def withdraw(self, account: int, money: int) -> bool:
        if account-1 >self.length-1 or self.accountNumber[account-1] < money:
            return False
        self.accountNumber[account-1] -=  money
        return True
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)