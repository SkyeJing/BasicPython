## Animal is-a object (yes,sort of confusing)look at the extra credit 
class Animal(object):
	pass

## is-a
class Dog(Animal):
	def __init__(self,name):
		## has-a
		self.name=name

## is-a
class Cat(Animal):
	def __init__(self,name):
		## has-a
		self.name=name
		
## is-a
class Person(object):
	def __init__(self,name):
		## has-a
		self.name=name
		
		##Person has-a pet of some kind
		self.pet = None

## is-a
class Employee(Person):
	def __init__(self,name,salary):
		## ?? hmm what is this strange magic?
		super(Employee,self).__init__(name)
		## has-a
		self.salary=salary

## ??
class Fish(object):
	pass

## ??
class Salmon(Fish):
	pass
	
## ??
class Halibut(Fish):
	pass
	
## rover is-a Dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = Person("Mary")