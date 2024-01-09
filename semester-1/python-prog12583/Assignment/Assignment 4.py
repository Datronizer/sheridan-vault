"""
1. Draw the UML diagrams for the following classes, as drawn below:
   Bus <-> Driver <-> Passenger
   Add two attributes and two methods in each class.
2. Write the code for each class in question 1.
   Then write the code that tests each attribute and method in each class.
3. Put the following classes in an inheritance tree. Do not write any code, just submit a diagram showing the classes.
   Add the attributes that follow, to the correct class in the diagram.

   Classes:
   Student
   Secretary
   GeographyProfessor
   Employee
   Person
   ArtsStudent
   AssociateDean
   EngStudent
   Professor
   EngProfessor
   

   Attributes:
   calculator
   dateOfBirth
   globe
   phoneExtension
   studyMaterial (lectures, powerPoint)
   desk
   multimeter
   paintBrush
   salary
   name
   employeeId
   address
   studentId

4. Write the code for the classes and test 4 of the attributes.
"""

class Driver:
   age: int
   
   def drive():
      putfootonpedal()
      
   
john = Driver(18)
john.age