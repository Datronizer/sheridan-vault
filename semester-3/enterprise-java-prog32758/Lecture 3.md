# Classes
A structure to model our business logic into our programs. A business logic in this case is the data and the logic encompassing it.

For Enterprise Java, a Class is a building block, and be well-defined, and must only be 1 object. Example: in a course catalogue software, we technically only need 1 object: a course. And this course object is defined by 1 single class.

It's important to differentiate operations performed on the course versus operations performed from the course to the database. In the case of the course being added to the catalogue, the methods should be on the course, but the operations invoked should affect only the database. The properties of said course should be well defined and initialised. 

The definition must include a constructor, necessary properties and methods, and getter-setter methods. Methods within the class should ONLY manipulate the object properties, NOT the logic for the actual application.

# Packages
At some point you'll have so many classes, keeping track of them would be harder than me fucking ur mom. This is when you should organise your classes. For Java, you can put all of them into a package. 

For a package, you should group only like elements and related elements. This helps you keep track of what does where and isolate the packages to their little spaces, thus preventing a lot of unnecessary cross-interactions.

**Example:**
Let's take an example of a typical Client-Server Architecture. We can break this down into 2 components, the Client and the Server. For each of these we can define smaller parts, example:

**Server needs:**
- Business objects (Model)
- Business/Application logic (Controller)

**Client needs:** 
- Web pages (View)

An example of how we can set up the project is using the MVC. We can have the Model being all Business Objects. Next is the Application Logic (Controller) which manipulate the Business Objects, which is put into a separate component/package. Finally, all the web pages are put into a separate package to make up the View component.

Of course this can be broken down further, as mentioned [[semester-3/enterprise-java-prog32758/Lecture 2|last lecture]] where the View can have static/dynamic pages.
# MVC in Enterprise Java
## Model - Classes
### Standard Class Structure
Model is a class that defines objects in an application. The structure of the standardised model is as such:
1. Header (`public class blahblah`)
2. Properties
	- Instance Variables (property accessible only by the initialised instance)
	- Class Variables (property accessible by all instances of this class--defined with `static`)
3. Methods
	1. Constructors:
		- Method used to (*surprise surprise*) construct the class (*wowwww*)
		- Must be public, has no return type, name must match name of class
		- Has 2 types:
			- Noargs: Constructor with no arguments
			- Args: Constructor with arguments (mmm naming conventions)
	2. Setters:
		- Method used to (*guess what*) set/change property values (*wowwwwww*)
		- No return type, takes arg of same type as property and sets that property the value of said arg.
	3. Getters:
		- Method used to (*guess wh- okay this joke is getting stale*) get/return value of a property
		- Returns the property specified in the arg
	4. Manipulators (*my ex jajajajajajaja*)
		- Takes an input and pipes it into a different output.
	5. Overridden methods: 
		- Methods that get overridden from the superclass. 

There is a difference between `Model` and `model` in Enterprise Java. `model` is an instance of `Model`.
### Java Bean 
A resuable software component that can be used to encapsulate many objects into a single object (Java class as a Java Bean)

Java Bean follows certain rules, them being:
1. (optional) JavaBeans implement the `Serializable` interface
	- Tagging interface in java.io that indicates a class contains getters and setters that another class can use to read/write an object's instance variables to/from a consistent source
	- This allows the data to be stored in secondary storage (database/local file/etc.)
2. All properties must be `private`
3. Every class must have a no-arg constructor that sets all instance vars to default values:
	- `0` for numeric
	- Empty string for `String` types
	- `false` for bools
	- New instance of object for all other reference types
4. For each private property, there must be 1 getter and 1 setter. Naming convention should be followed.

Any class that matches this exact descriptor is called a [*Java Bean*](https://docs.oracle.com/javase/tutorial/javabeans/) (*again, who named this shit?*).

Example:
An example of a JavaBean
```java
public class Student implements java.io.Serializable {
	// Properties:
	private String firstName = "";
	private String lastName = "";
	private int age = 0;

	// No-arg Constructor
	public Student() { }    // You don't need these since they apply implicitly by default

	// Getters
	public String getFirstName() { return firstName; }
	public String getLastName() { return lastName; }
	public int getAge() { return age; }

	// Setters
	public void setFirstName(String firstName) { this.firstName = firstName; }
	public void setlastName(String lastName) { this.lastName = lastName; }
	public void setAge(int age) { this.age = age; }
}
```

#### Enterprise Java Bean (EJB)
Slightly different from JBs. It is a class, written as a JB, but applications across organization uses this class. Basically a JB class that can be used across your whole enterprise.

Example:
```java
@Stateless
public class TestStatelessEjb {
	public String sayHello(String name) {
		return "Hello, " + name + "!";
	}
}
```

This class and its method can be used by every authorized application in the organization. Look at [Oracle](https://docs.oracle.com/javaee/6/tutorial/doc/gipmb.html) or [Stackify](https://stackify.com/enterprise-java-beans/) for reference.

## View - Thymeleaf
Java library, XML/HTML5 template engine able to apply transformations to display data/text produced by web apps. Main goal is to provide an elegant and well-formed way of creating templates.

To use it, you must include it as a project dependency, or you can manually do it. For how to do it, refer to the class presentation. 

All HTML files, by default, should be placed in the `src/main/resources/templates` folder. Of course, don't forget the [[Entry Point|index.html]] file.
### Model Atrributes
Do `th:text="${attributeName}"` as an attribute in your tag to display the value of the model attributes

Example:
```html
<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<body>
	Course Input Data:<br/>
	<p th:text="'Course:' + ${course.courseNumber}" />
</body>
</html>												
```

You can also use conditions in Thymeleaf to display models based on logic. To display element assuming element is true do `th:if="${condition}"` or otherwise false do `th:unless="${condition}"`. You can also do switch casing in Thymeleaf (*what the fuck*).

## Controller
As we know, the model is comprised of business objects, in our case, JavaBean classes. The Controller would begin by accepting a [[HTTP#Request|Request]], probably from a View element. We now need to process this data using some logic, in our case, Application Logic. To faciliate this, we will also use classes, but these classes are specialised. These special classes are called Controllers, whose task is to communicate between the View and Model.

The controller would Receive the Request from the View and process that into a Response. To process the Request, the controller would receive the View Input as its Parameter (`@RequestParam`) => manipulate that using the Business Model into a Response (computed Object) => send that Response

It is important to understand that the client doesn't *directly* send a data to the Controller. The Controller actually only process the data coming from the *Request* which is generated by the client. **There is no direct communication between the client and the Controller (at least for example 2-1)**.

