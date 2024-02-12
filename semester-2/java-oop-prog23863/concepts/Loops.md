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

# `foreach` loop
Although we call it a `foreach` loop, it's shown solely as a `for` loop, but instead of grabbing elements of a list based on index, it iterates directly through the list and grabs the item. 

In a way it's a `for` loop but for elements, rather than indexes. Example:

```
for (String s : names)
{
	System.out.println(s)
}

/**
 * This can be read as "For each string in the list `names`, assign it to
 * a variable s, then do something with this s." (In this case we print `s`)
 */
```