# Client-Server Communication
To facilitate communication between the client and the server, we will require the use of [[HTTP]]. The HTTP protocol will allow us a structured way to organize our data to prepare it to be sent from source to destination.

In this case, the source is the Client, which in this case is also a Web Browser and the destination is the Server running Apache-Tomcat.

More information regarding this is in the [[HTTP]] document.

But basically, an example of a URI is such
`https://www.google.ca/images/some-image-name-here.png?dateUploaded=blahblahblah`
- `https://` is the protocol
- `www.google.ca` is the web server
- `/images` is the application root directory
- `/some-image-name-here.png` is the resource I'm looking for
- `?dateUploaded=blahblahblah` is one key-value pair of a list of request parameters, separated from the URI by a `?`


Only 1 method to process 1 request (which makes sense, else it doesn't know which method to actually execute)

# MVC
Model - View - Controller

For reference, refer to this [official definition](https://www.oracle.com/technical-resources/articles/javase/mvc.html) by Java SE

- Model: Business Objects (Java Classes, organized and structured)
- View: All the web pages / User Interfaces
- Controller: Liaison between Model and View, communicates data between View and Model (Design to Classes and back).

There are 3 steps to making a web page. Making the project -> Making the Architecture -> Actually coding the server.

Let's look at the 3 steps represented the 3 components of the MVC model.
## Controller
In the `src/main/java` resides a bunch of "Business Objects", those being classes. SpringBoot apps will usually generate a main Class with only the main method with this method running in it: `SpringApplication.run(SomeClassName.java, args)`

To make a new Package, do New -> Package and choose the name of a new package. Assuming you're making a new Controller Package which is a subpackage of the original package, you should name it after the original package then `.controller`. Example: `ca.sheridan.truonchi.controller` for the original `ca.sheridan.truonchi` package.

To use a new Class that uses the subpackage you just made. Do New -> Class within the package you made, name your class whatever as long as it makes sense, then specify the package as the name of the package you just created.

When making a new class, you should annotate it with an [[Decorators|annotator]](Java's equivalence of a Decorator) that matches what your class is meant to do. Example: if your class is Controller, add `@Controller` right before the class declaration. Doing that will lock your class out from imports and turn it into a proper Controller class.
## View
All your view objects are in the `src/main/resources` directory. And they can separate into either a `static` page or a `template` page (yeah I know the naming convention is dumb as shit, just bear with me).

A static page remains constant over time. A template page contains a template such that the data it receives can dynamically change the look/view of the page. It does this by taking an input, and returns a template response based on the Server's [[HTTP#Response|response]].
## Model
The Model here would be the business objects which are already apparent in the classes that make up the project. The data in these classes can be changed, updated, and their methods can be called, then communicated to the controller, who will facilitate updates to be sent to the view to dynamically change the page. 

This whole process is seamless and is almost instant (unless you're a developer at Riot Games, in which case, fuck you, fuck your League client, and your whole company).
