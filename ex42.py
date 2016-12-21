## animal is-a object(yes,sort of confusing) look at the extra credit
class Animal(object):
	pass

## dog is-a object 
class Dog(Animal):

	def __init__(self, name):
		## dog has-a name
		self.name = name

##cat is-a object
class Cat(Animal):

	def __init__(self, name):
		##cat has-a name
		self.name = name
		
##person is-a object
class Person(object):

	def __init__(self, name):
		##person has-a name
		self.name = name
		
		## Person has-a pet of some kind
		self.pet = None
		
##employee is-a person
class Employee(Person):

	def __init__(self, name, salary):
		## emloyee has-a name hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## employee has-a name
		self.salary = salary
		
##fish is-a object
class Fish(object):
	pass
	
##salmon is-a fish
class Salmon(Fish):
	pass
	
##halibut is-a fish
class Halibut(Fish):
	pass
	
	
## rover is-a Dog
rover = Dog("Rover")

##satan is-a cat
satan = Cat("Satan")

##mary is-a person
mary = Person("Mary")

##satan is-a pet of mary
mary.pet = satan

##frank is-a employee
frank = Employee("Frank",120000)

##rover is-a pet of frank
frank.pet = rover

##flipper is-a fish
flipper = Fish()

##crouse is-a salmon
crouse = Salmon()

##harry is-a halibut
harry = Halibut()
