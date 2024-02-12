An arrayList is basically (in the simplest way possible) an Array with the properties of a list. What does that mean?

An [[array]] in Java is an immutable structure whose length cannot be changed as it is preallocated in memory. But ArrayLists are mutable. You can add or remove elements from an ArrayList and change its size dynamically.

Unfortunately, this is a subclass of the `java.util` class. Thus, to use ArrayList, you'll need to import it.

To declare an `ArrayList` of the name `list`, do:
```
ArrayList<Integer> list = new ArrayList<Integer>();

list.add(12);
list.add(42);
list.add(0);
list.add(-53);

System.out.print(list.get(2))    // this prints 0 since its index is 2
System.out.print(list.size())    // this prints 4 (similar to array.length)
```

