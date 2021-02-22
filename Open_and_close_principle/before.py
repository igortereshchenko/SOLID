from Single_responsibility.after.Account import Account

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

class Discount:

    def __int__(self, product:Product, account:Account):
        self.product = product
        self.account = account

    # 10% for any account
    def get_discount(self):
        return self.product.price*0.9

    # 90%
    def get_diccount_vip(self):
        return self.product.price*0.1

    # VS

    def get_universal_discount(self):
        if (self.account.name=='Bob'):
            return self.product.price*0.1
        elif (self.account.name=='Boba'):
            return self.product.price * 0.2

        return self.product.price*0.9
