```python
import abc
from math import prod
import time
from enum import Enum


class Product:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, arg):
        self._name = arg

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, arg):
        assert isinstance(arg, float)
        self._price = arg

class Chips(Product):
    def __init__(self) -> None:
        super().__init__('Chips', 20)

class Coke(Product):
    def __init__(self) -> None:
        super().__init__('Coke', 35)


class Slot:
    def __init__(self, x, y, nxt=None, product=None) -> None:
        self.x = x
        self.y = y
        self.next = nxt
        self.product = product

    @property
    def isEmpty(self):
        return self.product is None

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, arg):
        assert isinstance(arg, Product) or arg is None
        self._product = arg


class VendingMachine:
    isInstantiated = False
    
    def __init__(self, rows, cols, maxSlotLen) -> None:
        if VendingMachine.isInstantiated:
            raise
        VendingMachine.isInstantiated = True
        
        self.maxSlotLen = maxSlotLen
        
        slots = []
        for x in range(rows):
            row = []
            
            for y in range(cols):
                length, head, curr = 1, Slot(x, y), head
                while length < self.maxSlotLen:
                    newSlot = Slot(x, y)
                    curr.next = newSlot
                    curr = curr.next

                row.append(head)

            slots.append(row)

        self.slots = slots
        self.purchases = []


    def addProduct(self, row, col, product):
        slot = self.slots[row][col]

        curr = slot
        while True:
            if curr.isEmpty():
                curr.product = product
                return
            curr = curr.next
        
        raise NoSpaceLeftError()

    def dispenseProduct(self, row, col):
        product = self.slots[row][col]
        self.slots[row][col] = self.slots[row][col].next
        
        return product

    def addPurchase(self, user, product, payment):
        self.purchases.append({'user': user, 'product': product, 'payment': payment})

    def purchaseProduct(self, user, row, col, paymentType):
        payment = PaymentFactory.createPayment(paymentType)
        payment.checkout()  # maybe an async call is made
        
        while payment.status not in (PaymentStatus.SUCCESSFUL, PaymentStatus.FAILED):
            time.sleep(1000)

        if payment.status is PaymentStatus.FAILED:
            return
        
        self.addPurchase(user, self.slots[row][col], payment)
        return self.dispenseProduct(row, col)

class PaymentType(Enum):
    CARD = 1
    UPI = 2

class PaymentStatus(Enum):
    INITIATED = 1
    PROCESSING = 2
    SUCCESSFUL = 3
    FAILED = 4

class Payment(abc.ABC):
    @abc.abstractmethod
    def checkout(self):
        pass

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, arg):
        self._status = arg
        

class CardPayment:
    def __init__(self) -> None:
        self.type = PaymentType.CARD

    def checkout(self):
        pass

class UPIPayment:
    def __init__(self) -> None:
        self.type = PaymentType.UPI

    def checkout(self):
        pass

class PaymentFactory:
    @classmethod
    def createPayment(self, type) -> None:
        if type is PaymentType.CARD:
            return CardPayment()
        elif type is PaymentType.UPI:
            return UPIPayment()
```