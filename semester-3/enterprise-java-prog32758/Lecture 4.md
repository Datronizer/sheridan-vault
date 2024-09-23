Project Object Model (POM), how the project will be built, what dependencies are needed, etc.

# Web app life cycle
1. Devlopment
2. Deployment
3. Un-deploy 

An average web application lasts around 5-7 years, from conception to un-deployment

# Deployment
Prior to Spring Boot, Java web applications used to be deployed manually. You had to write your own deployment script and use JSP (Java Servlet Page) for your template sites.

After Spring Boot was made, there was an option to use Web Application Frameworks to support the development of applications including web services, web resources, and web APIs. It became the standard way to deploy web apps on the World Wide Web.

Using Springboot, we can use Deployment Descriptors to tell SPring Boot to compile our objects as the aforementioned bits and pieces.
## Parameters
Input(*adj*) data for a controller, can be one of the following
- Input data form the HTTP Request Object
- Application Initialization/context data

Params define input data from a web page as request parameters for a method in the controller class. Options include:
- Request Params: each input vlaue is a param and business objects are created in the mapped method of the controller class
- psasld
- aksldn
	- ksdjdfk
- 
## Attributes
Key-value pair, name being a string, value being an Object, ***always***. The scope of which can be a request, session, or the application context => passed to the controller.

An attribute is an object (computed business objects), which are re-communicated back to the client, in the body of the [[HTTP#Response|Response]], and can be set as one of these 3 servlet API objects.
- HTTP Request (Servlet object)
- HTTP Response
- *idr what this is*

# ThymeLeaf
## Introduction
Java library, XML/HTML5 template engine able to apply transformations to display data/text produced by web apps. Main goal is to provide an elegant and well-formed way of creating templates.

To use it, you must include it as a project dependency, or you can manually do it. For how to do it, refer to the class presentation. 

All HTML files, by default, should be placed in the `src/main/resources/templates` folder. Of course, don't forget the [[Entry Point|index.html]] file.
## Displaying Model Attributes
There are 2 types of model attributes for ThymeLeaf, *Simple Atrributes* or *Collection Atrributes*.
### Displaying a Simple Model Attribute
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

- `xmlns`: XML Namespace
	- in our case, this will download the templates and components from Thymeleaf to execute without needing a separate installer (basically an online version of `node_modules`)
	- `th:text`
### Display a Collection Model Attribute
For this, please refer to the powerpoint (this is really long)
## Thymeleaf fragment
Think reusable [[component]]. That's basically what a Thymeleaf fragment is. It's just a piece of HTML that can be defined once, and reused on multiple pages. 

Typical examples would be headers, footers, and navbars.
### Defining fragments
Put your fragments in `src/main/resources/templates/fragments/fragmentName.html`

Then do:
```HTML
<someTag th:fragment="FragmentName">
	{...children}
</someTag>
```

### Using fragments
There are 3 ways to use these fragments
- Insert
- Replace
- sdkajsd

Example:
```HTML
...

<tag1 th:replace="/link/to/file.html"::"fragmentName" />
<tag1 th:insert="/link/to/file.html"::"fragmentName" />

...
```
## Conditionals
You can also use conditions in Thymeleaf to display models based on logic. To display element assuming element is true do `th:if="${condition}"` or otherwise false do `th:unless="${condition}"`. You can also do switch casing in Thymeleaf (*what the fuck*).

