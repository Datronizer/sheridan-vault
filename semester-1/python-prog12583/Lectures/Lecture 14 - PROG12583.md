# Classes
WOO YEAHHH BABY ITS TIME FOR CLASSES

A `class` is a type of object whose attributes and methods are defined by the user. Unlike **global attributes**, a.k.a. what we have been doing the whole time, a class attribute is a variable within the scope of that class. Meaning, we can instantiate them over and over and give each instance of that class a different value for its attributes. Another different thing is that you can call a global variable within a class, but not vice versa. Whatever is in that class stays in that class.

As we have discussed [[Lecture 13 - PROG12583|last class]], objects are related, either through inheritance, instantiation, or are not related at all. In the UML diagram, this is represented as such [please insert photo here].
## Keywords
## Initialization
When you define a class, you must also give it a blueprint so it knows how to arrange these values upon input. All initialization uses `def __init__(self, [...someVariables])`. Example:
```
class Cat:
	def __init__(self, breed, furColor):
		self.breed = breed
		self.furColor = furColor
```
Here `self` is the object that is being created. The `breed` and `furColor` arguments are what we input. The `self.breed` and `self.furColor` are us assigning the arguments into the attributes.

Think of it like one of those block toys where we try to fit shapes into a frame. `self` is the whole toy. `self.breed` and `self.furColor` are the frames you're supposed to insert things in. `breed` and `furColor` (the arguments) are the wooden blocks. Of course you can put a triangle into a square block (`self.breed = furColor`), but why would you do that? That would just be confusing!
### Instance Variable
An instance variable is a variable that is initialized for every instance. It can be different from instance to instance and can be changed upon initialization.

Another word for this is **attribute**, and guess what? `self.breed` and `self.furColor` are attributes. 
### Class Variable
A class variable is a variable that is initialized with every single created instance. For example, you can have an instance counter to check how many times this class has been initialized.
```
class Cat:
	totalCats = 0
	def __init__(self, breed):
		this.breed = breed
		Cat.totalCats = Cat.totalCats + 1

cat1 = Cat("Calico")
cat2 = Cat("Tabby")

print("There are", Cat.totalCats, "cats.")     

>> There are 2 cats.
```

