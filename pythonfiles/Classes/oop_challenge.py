# class Simple():


#     def __init__(self,value):
#         self.value = value

#     def add_to_value(self,amount):

#         self.value = self.value + amount
#         print(f'We just added {amount} to your value ')


# myobj = Simple(300)

# myobj.add_to_value(500)

# print(myobj.value)


class Account():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account owner: {self.owner}\n Account Balance: {self.balance} "
    
    def add_to_value(self,deposit):
        self.balance = self.balance + deposit
        # self.balance += deposit
        print(f"We have just added {deposit} to your bank account ")
    
    def remove_from_value(self,withdraw):
        if withdraw <= self.balance:
            self.balance = self.balance - withdraw
            # self.balance -= withdraw
            print(f"We have just removed {withdraw} from your account ")
        else:
            print('Funds Unavailable! ')
        
        
    


acct1 = Account('Jose', 3000)

print(acct1.owner)
print(acct1.balance)

acct1.add_to_value(8000)
acct1.remove_from_value(200)
print(f"Balance left is {acct1.balance}")
    

    




