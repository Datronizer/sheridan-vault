# Introduction
To force a sequence to divert based on a condition, we add an if-statement. An `if` only takes 2 values: `true` and `false`. And we can evaluate boolean expressions and store the `true`/`false` values into variables.

Here's an example:
```
if (rain)
{
	takeTheBus()
}
else
{
	walk()
}
```

What about evaluating expressions? Well, we can do so as well!
```
int num1 = 5;

System.out.println(num1 == 10)    // false
System.out.println(num1 == 5)     // true
```
# Operators
## Comparison operators
> < == != !
## Compound comparison operators
You can stack comparison operators to evaluate if something is less than/greater than or equal to some other thing. Example: 
```
3 >= 2    // true
3 <= 2    // false

2 <= 2    // true
2 >= 2    // true
``` 

If you're thinking what I'm thinking, and you have problem reading things (also me), you'd think this is a bad idea because it clutters up the code. You know what I think is good? Don't stack the evals and just negate the inverse of the eval i.e. `(1 + 1 >= 2)` is equivalent to `!(1 + 1 < 2)`
## Logical operators
Oh boy, "logic", don't that sound familiar? Yes it is. We talked about this in great detail in [[Boolean Algebra]], so we'll just briefly look at some operators that exist in most languages.
- `&&` (AND)
- `||` (OR)
- `!` (NOT)
- `^` (NOR)
## Ternary operator
Oh man, how badly do you want to fuck your code up? Because I got you.

There is a shortcut to if-statements that you could do. Suppose I have the following:
```
if ( 1 + 1 > 3 )
{
	System.out.println("1 + 1 > 3 since when?");
}
else 
{
	System.out.println("1 + 1 is not greater than 3");
}
```

I can change that to a shorthand 
```
String statement = ( 1 + 1 > 3 ) ? "1 + 1 > 3 since when?" : "1 + 1 is not greater than 3"

System.out.println(statement)    // "1 + 1 is not greater than 3"
```
# Else-if
Insert YandereSim or Undertale if-else nightmare stack here.

In any case, an `if` statement can be checked for other conditions aside from the original one. This is when we use an `else` block. But what if you want to check for something before resorting to the catch-all `else` block?

You use `else if`.

```
int a = 2;

if (a < 2) {
	System.out.println("a < 2");    // skips
} else if (a == 2) {
	System.out.println("a is 2");   // prints
} else {
	System.out.println("a > 2");    // block not reached
}
```


