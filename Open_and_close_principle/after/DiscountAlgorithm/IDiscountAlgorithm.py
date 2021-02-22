from Open_and_close_principle.after.Product import Product
from Single_responsibility.after.Account import Account


class IDiscountAlgorithm:

    def calculate(self, product: Product, account: Account):
        raise NotImplementedError
