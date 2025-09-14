# Javascript (JS)
## Preamble
So, we're finally here, to this shitty language.

Let's start by saying that I hate this language and all the hostilities I hold here are not necessarily true for everyone. Some love this language, a lot hate it, but we can all agree that it MAKES MONEY.
## Introduction
### History
### Usage
To add JS into your HTML, add a `<script>` tag to your `<head>`, for example:
```HTML
<html>
	<head>
		<script>
			someJsFunction()
		</script>
	</head>
	<body>
		...
	</body>
</html>
```

Within this tab, you can place JS functions %% Link this to a `function` header rather than article %%, classes, methods, etc. Ideally you should keep classes separate in `.js` files rather than in here. Better to keep functions here only. More on this later.
### Import
As mentioned earlier, you can split your JS classes and functions into their respective folder, whether it be for [[Refactoring]] or for personal reasons. To do so, create a file ending with `.js`, for example, `myScript.js`. 

Now we can import this through one of two ways.
- Through relative path
- Through absolute path

You probably remember the [[path]] concept from HTML or Linux, it's quite commonplace in coding. In any case, you'd reference the JS file like so
```
<script src="myScript.js" />
// or
<script src="https://example.com/path/to/myScript.js" />
```

### Display
Of course sometimes you want to display some information to the user or other developers using the site, there are a few ways to do this.
- `innerHTML`
- `document.write()`
- `alert(string | number)` this gives you a pop-up of the entered message.
- `console.log(string | number)` will log message straight to the console
	- To access the console, hit `Inspect element` or hit F12.

## Loop
Like other languages, JS has a [[concepts/compsci/coding/middle-level/Loops#`for` loop|for loop]] and a [[concepts/compsci/coding/middle-level/Loops#`while` loop|while loop]]. But what you're probably not expecting is that it also has a [[concepts/compsci/coding/middle-level/Loops#`do-while` loop|do-while loop]]. Example:

```
let x, y, z; 
x = 5;       
do {
	y = parseInt(prompt("age?"));
} 
while (isNaN(y))

z = x + y;
document.write("Age in 5 years" + z);
```

### Declarations
Unlike other languages, JS does not require declaring [[Simple Data Types]], but we do have to declare whether the variable is `const`, `var`, or `let` a.k.a. [[Type qualifiers]].
# Debugging
To debug JS, add `debugger` to the line of code you wish to start the debugging. Then go straight to the browser, and hit F12 to inspect elements. If you've done everything right, the browser should automatically pause loading at the debugger line. 

Now you can do debugging as you would in VSCode.

Don't forget to delete the `debugger` line after you're done debugging. Trust me.