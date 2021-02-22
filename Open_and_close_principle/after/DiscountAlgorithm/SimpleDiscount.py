from Open_and_close_principle.after.DiscountAlgorithm.IDiscountAlgorithm import IDiscountAlgorithm
from Open_and_close_principle.after.Product import Product
from Single_responsibility.after.Account import Account

class SimpleDiscount(IDiscountAlgorithm):

    def calculate(self, product: Product, account: Account):
        return product.price * 0.9

