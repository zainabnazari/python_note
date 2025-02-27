# file name: main_file.py
# this file is called main_file and contains the main condition

class Person:
  def function(self, name, age):
    self.name = name
    self.age = age


if __name__ == "__main__":
	p1 = Person()#Since we don't have an __init__-function specified, we cannot give parameters on instantiation*. p1 does not have any attributes (name or age) yet.
	p1.function("John", 36)#If we want to specify attributes, we need to call an extra function.
	print(p1.name)
	print(p1.age)
	'''
	* instantiation: In programming, instantiation is the creation of a real instance or particular realization of an abstraction or template such as a class of objects or a computer process.
	'''

"""
When we run this file, the output is:
John
36
"""
