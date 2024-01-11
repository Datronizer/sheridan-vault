# Introduction to Java
Before we get into the language, let's first identify what a Java file looks like. Typically it would be have the extension `.java`, i.e. `urmom.java` (see what I did there?)
## "Hello, world!" in Java
Prepare yourself for the most fuckass syntax known to man.
To do a simple "Hello, world!" print, do as such:
```
public class fileName
{
	public static void main(String[] args)
	{
		System.out.println("Hello, world!");
	}
}
```

Let's break down what's going on.
- Line 1 declares a class whose name is the same as that of the file containing it. Naming it this way allows the system to initialize the class using the file name. Example, file name is `urmom.java`, then your class declaration should be `public class urMom { ... }`
- Line 3 creates a `static` method that returns `void` (not returning anything), whose name is `main`. It takes `args` as an array arguments of the type `String`, in this case is `String[]`.
- Line 5 tells the system to tell the `System`, go into the class `out`, and do `println`. Printing syntax would be similar to Python (and vice versa).
- At the end of each statement is a semicolon, unlike Python (blegh).
## Inline computation
Turns out printing is pretty consistent across languages! Look at what we can print below.

```
public static void main(String[] args)
{
	int a = 1
	int b = 7
	int c = a + b

	System.out.println(c)    // 8
}
```

As you can see, unlike Python, Java is [[strongly typed]]--meaning variable types must be properly defined. There is a historical reason for this of course. A reason that we have previously discussed in [[Memory & Compiler Maps]] by professor Zaki Asmat.