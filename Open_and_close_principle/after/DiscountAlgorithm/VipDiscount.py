from Open_and_close_principle.after.DiscountAlgorithm.IDiscountAlgorithm import IDiscountAlgorithm
from Open_and_close_principle.after.Product import Product
from Open_and_close_principle.after.DiscountAlgorithm.SimpleDiscount import SimpleDiscount
from Single_responsibility.after.Account import Account

class VipDiscount(IDiscountAlgorithm):

    def calculate(self, product: Product, account: Account):

        if (account.name == 'Bob'):
            return product.price * 0.1
        else:
            simple_discount = SimpleDiscount()
            return simple_discount.calculate(product, account)


