# Lazy evaluations
## In laypeople's terms
In Java, statements are lazily evaluated (not always). What does this mean? 

Say you're at home watching TV and mom told you to wash the dishes by the time she gets home. Now there are 2 ways around this.
1. You wash the dishes as soon as the command is issued
2. You wait until she's almost home to wash the dishes

Obviously, any sane person would... watch TV and wash the dishes after, duh. Why would I want to wash dishes first?

In this case, statement 1 would be an **eager evaluation** and statement 2 would be a **lazy evaluation**. A lazy evaluation is only executed when it is needed. This saves memory and processing power.
## Technical definition
I don't know the actual definition, good luck lol

## Short-circuit evaluations
A short circuit evaluation is simply an evaluation that is evaluated prematurely in order to chop off redundancy. This is not an official definition but it's easier to understand.

For example:
```
System.out.println(true || false)    // Always true
System.out.println(false && true)    // Always false

System.out.println(false && (true || false))    // Always false
```
For the 3rd statement, since we know that the statement would evaluate `false` anyways, there is zero need to evaluate the rest. Hence Java would flag the statement and tell you to delete the redundancy.

You're probably wondering why short circuit evals are in this section. Well, it's *technically* a really specific case of lazy eval. This [link](https://aashni.me/blog/lazy-evaluations-and-short-circuit-logic-in-javascript/) does a really good job at explaining (but holy shit who the fuck uses cyan for code???).

If you're looking for a tl;dr of how it works, I will explain it.
#### tl;dr
- **Recall:** Java expressions are evaluated top down, left to right per line. 
- Suppose you have the following: 
	- `func1() { return true }`
	- `func2() { return false }`
	- `func3() { return true }`
- Suppose those 3 are like super complex functions that take hours to solve for each one, but we know what it returns.
- Then this expression `System.out.println(func1() || !(func2() || func3()))` will be evaluated as such:
	- Java solves `func1()` and gets `true`.
	- Java sees an `OR` operator (`||`)
	- Java goes "wait a minute, wtf, I don't need to solve the rest, it's always `true` because the LHS is `true`!"
	- Java short-circuits the expression (ignores the rest) and returns `true`.

Hence this is a lazy evaluation because Java didn't need to solve the other 2 functions.


%% TODO: Find the appropriate link and paste it here. If it exists. %%