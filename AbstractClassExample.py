# Python program invoking a
# method using super()

import abc
from abc import ABC, abstractmethod

class R(ABC):

	#@abstractmethod
	def rk(self):
		print("Abstract Base Class")
		pass


class K(R):
	def rk(self):
		super().rk()
		print("subclass ")

# Driver code
r = R()
r.rk()

k = K()
k.rk()
