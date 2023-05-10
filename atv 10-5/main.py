import abc


class Product(metaclass=abc.ABCMeta):
    pass
class  NullProduct(Product):
    pass


class ProductManager:
    pass


class PurchaseProces(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def processPurchase():
        pass
    def validatePayment():
        pass
class PurchasePhone(PurchaseProces):
    def processPurchase():
        pass
class PurchaseTablet(PurchaseProces):
    def processPurchase():
        pass


class ProductFatory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def createProduct():
        pass
class PhoneFactory(ProductFatory):
    def createProduct():
        pass
class TabletFactory(ProductFatory):
    def createProduct():
        pass


