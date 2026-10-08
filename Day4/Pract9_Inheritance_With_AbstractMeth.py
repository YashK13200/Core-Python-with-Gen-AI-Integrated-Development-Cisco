'''
>>> from abc import ABC,abstractmethod
>>> 
>>> class Payment(ABC):
...     @abstractmethod
...     def pay(self):
...         pass
...         
>>> class CreditCard(Payment):
...     def pay(self):
...         print("Paying using CC")
...         
>>> class UPI(Payment):
...     def pay(self):
...         print("Paying using UPI")
...         
>>> cobj = CreditCard()
>>> upiobj = UPI()
>>> 
>>> Payment()
Traceback (most recent call last):
  File "<python-input-848>", line 1, in <module>
    Payment()
    ~~~~~~~^^
TypeError: Can't instantiate abstract class Payment without an implementation for abstract method 'pay'
>>> 
>>> 
>>> 
'''
