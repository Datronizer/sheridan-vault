# Sets
## Overview
Oh baby now this is my jam.

Sets are one of the fundamental building blocks of mathematics. Specifically modern math. Calculus, Computer Science, Physics, and Abstract Algebra simply would not exist without sets. Sets are quite basically the "atoms" of math.
## Definition
A formal definition of a **set** is that it is an unordered collection of **distinct** objects.
- These **distinct** objects are called **elements**
- A set is said to **contain** its elements (though you will not hear this exact phrase like ever again)
- A set must also be **well-defined** [[#^1]]

By that definition, a basket of distinct candies is a set, a box of scraps is a set, but a set of children's toys should not have a shotgun because, well, that's not a children's toy. 

But what if I have a set and it contains something that may or may not be an element of a set? Let's say I have a set of drinks, and within it is a swig of moonshine. Some people may see that as a drink, while some see that as molotov fuel against a certain apartheid state. So it isn't clear that this is a drink. Then this set is NOT well-defined. ^1
## Notations
### Standard notation
There are a few simple rules for notating a set. These help keep things uniformed and easy to understand.
1. Sets are usually designated by a capital letter.
2. Elements of a set are usually designated by lowercase letter.
3. Curly braces are usually used to enclose the elements of a set.
4. Elements are comma-separated.

To say some element a is an element of set A we do $a \in A$.
To say some element a is NOT an element of set A we do $a \not\in A$.

Example:
- The set V of all vowels in English is $V = {a,e,i,o,u}$
- The set I of all odd positive integers less than 100 is $I = {1,3,5,...,97,99}$
### Set-builder notation
Guess what this notation does. No, go on, guess. That's right, it BUILDS SETS WHAT THE FUCK.

In my opinion, the set-builder notation is like a blueprint for you to build a set from. You don't need to specify the elements, just the property/ies of all elements of the set.

Example:
The set of all positive integers less than 10: 
$$
\begin{align}
O &= \{x|x\text{ is a positive integer less than 10}\} \\
&or \\
O &= \{x \in \mathbb{Z}^+ | x < 10\}
\end{align}
$$
## Standard sets
Here are a few sets that are "standard" and are common in mathematics, especially Discrete Math:
- $\emptyset \text{ or } \{\space\}$ denotes an empty set
- 
## Other sets
### Empty set
A set with no elements is a **null set** or an **empty set**. Usually in higher mathematics we use "empty set" more because it makes more sense. Also empty sets is a crucial component of [[topological spaces]]--a topic we will definitely NEVER get into.

You can define a set A as an empty set with the following notation:
$$
A = \{\emptyset\}
$$
It's an O with a slash through. Pretty neat huh?
### Infinite set
A set with infinitely many elements is an infinite set. To describe this set with use the following notation. For example, for the set of all natural numbers:
$$
\mathbb{N} = \{1,2,3,4,...\}
$$
Ellipses mark that this set is ongoing and there may be more elements.
### Singleton
A set with **exactly** 1 element is a single set--more commonly called a **singleton**. You don't need a specific notation for this one. Just know that singletons are very important in the field of abstract algebra AND computer science. Yes, I have used them way too many times.
### Power set
A power set $\mathcal{P}$ of a set $S$ is a set of all sets that can be formed with the elements of $S$. A way to look at this is that $\mathcal{P}(S)$ is a set of all possible combinations of elements that composes set $S$.  For example, for the set $A = {1,2,3}$, the power set $\mathcal{P}(A) = \{\emptyset, \{1\}, \{2\}, \{3\}, \{1, 2\}, \{2, 3\}, \{1, 3\}, \{1, 2, 3\}\}$.