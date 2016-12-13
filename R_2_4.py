# Write a Python class,Flower, that has three instance variables of typestr,int,andfloat, that respectively represent the 
# name of the flower, its num-ber of petals, and its price.  
# Your class must include a constructor methodthat initializes each variable to an appropriate value, 
# and your class shouldinclude methods for setting the value of each type, and retrieving the valueof each type.

class Flower:
	def __init__(self, name, number_petals, price):
		self._name = name
		self._number_petals = number_petals
		self._price = price

	def set_name(self, name):
		self._name = name

	def get_name(self):
		return self._name

	def set_number_petals(self, petals):
		self._number_petals = petals

	def get_number_of_petals(self):
		return self._number_petals

	def set_price(self, price):
		self._price = price

	def get_price(self):
		return self._price



def main():
    flower = Flower('orchid', 3, 50)
    print 'total # of petals ', flower.get_number_of_petals()

if __name__ == "__main__":
    main()