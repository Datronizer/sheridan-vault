# `for` loops
# `while` loops
# `do-while` loops
This is a post-check loop. Meaning it will run everything inside `do` once before executing `while` which would then check the condition. Example:
```
int counter = 0;

do {
	System.out.print(counter: ",");
	counter++
} while (counter < 5);

> 0, 1, 2, 3, 4,
```
 Don't let the output fool you, although they both have the same output, they are fundamentally different. One applies an if-check before the `do` while one applies it after. 