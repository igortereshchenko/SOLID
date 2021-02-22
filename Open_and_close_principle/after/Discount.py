from Open_and_close_principle.after.DiscountAlgorithm.IDiscountAlgorithm import IDiscountAlgorithm
from Open_and_close_principle.after.Product import Product
from Single_responsibility.after.Account import Account

class Discount:

    def __int__(self, product: Product, account: Account, discount_algorithm: IDiscountAlgorithm):
        self.product = product
        self.account = account

        self.discount_algorithm = discount_algorithm


    def get_discount(self):
        return self.discount_algorithm.calculate(self.product, self.account)


