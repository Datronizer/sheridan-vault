# Inputting in Java
To receive user input in Java, we must tell the compiler to wait for input. How do we do that?

For Java, we need to import `java.util.Scanner`. Do this:
```java
import java.util.Scanner;

public class scanner {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        System.out.println("Type in a word: ");    // prompts user to type
        String word = keyboard.next();             // collects input as token
        System.out.println("You typed " + word);   // outputs the first word typed
    }
}
```

