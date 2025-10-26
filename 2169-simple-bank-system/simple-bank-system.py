class Bank(object):

    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self.balance = balance
        self.n = len(balance)

    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        # Validate account numbers
        if not (1 <= account1 <= self.n and 1 <= account2 <= self.n):
            return False
        
        # Validate balance of source account
        if self.balance[account1 - 1] < money:
            return False
        
        # Perform transfer
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        # Validate account number
        if not (1 <= account <= self.n):
            return False
        
        # Deposit money
        self.balance[account - 1] += money
        return True

    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        # Validate account number
        if not (1 <= account <= self.n):
            return False
        
        # Check if sufficient balance
        if self.balance[account - 1] < money:
            return False
        
        # Withdraw money
        self.balance[account - 1] -= money
        return True
