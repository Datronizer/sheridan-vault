## Memory limitations
Try punching $69!$ into your calculator, now do $70!$. You'll soon see that this is not possible. The reason for this is because calculators run on buses and memory chips. These chips have a limit to how much they can store/compute. The current limit right now is $10^99$, but that is hugeeeee compared to the first calculators: 99. Yes, only 99, less than 100. We call this a **chomp** because, you know, chomp (this is also placeholder numbers, it's technically FF = 256, not 99. It's also a "byte". But this example is easier to grasp).

So how did we get from there to what we have nowadays? Well, suppose one bus unit can do up to 99. What if we put them side by side? We would, instead of getting 198, we get 9999. The reason we get this much is that we only need to use the digits, rather than the count. This juxtaposition allows for more numbers to be **displayed**. Keyword here is **display** because we are can display more numbers and improve computations/storage.

Over time we realize we can do more with this. What if I want to compare two things? Well, we need to figure out the logistical issue with this idea. Suppose I want to compare 23 against 5000. I have to use a 1-chomp bus and a 2-chomp bus, and I have to physically wire them together. This doesn't seem practical because that might require too many modifications, also we are working with 2 different systems, so that's even more impractical. 

We could just use a 2-chomp bus to accommodate all the numbers and that would solve the problem. Except it's now very physically wasteful. That's too much hardware for a bunch of numbers that are going to be used as placeholder anyways. I could write $2347$ but I could also write $0017$. Now I'm wasting 2 slots for a feature I might not use too often.

Scientists came up with a solution. We can take a big number and chop it up into smaller numbers. $2347 = 23 + 47$. Now we can fit 2-chomp numbers into a 1-chomp system. This is the basis of modern memory design.

A block of memory, think RAM stick, has different "cabinets" where it stores data. These "cabinets" are formally known as "addresses", this is the 0x00000342 whatever thing you see in computers. Those are addresses the computer can use to access the information stored in the memory.

This table will help you visualize how the data is stored.
Say we have 3 variables:
- type of data = short | var name = s0 | value = 1234 | byte# = 2
- type of data = byte | var name = b0 | value = 78 | byte# = 1 (duh, it's a byte)
- type of data = int | var name = i0 | value = 88990011 | byte# = 4

| Address | Byte | Var     |
| ------- | ---- | ------- |
| 0       | 12   | s0      |
| 1       | 34   | s0      |
| 2       | 00   | "break" |
| 3       | 88   | i0      |
| 4       | 99   |         |
| 5       | 00   |         |
| 6       | 11   |         |
| 7       | 00   | "break" |
| 8       | 78   | b0      |
| 9       | 00   |         |
| etc.    | ...  | ...     |

Python allocates some memory for your variables **based on their data types**. When you declare a variable in other languages, you must also declare a type so that the interpreter/compiler can allocate room in its memory. A `00` with **no variables** denotes a break, meaning whatever after it is a new variable.

Often times, it, as well as us, overshoot the allocation and waste memory. Compare a `short` of value `55` and an `int` of value `55`. The `short` will just have 1 address of size 1 chomp. The `int` would have a size of 4 chomps because it needs to allocate extra room as `00 00 00 55`. This wastes a ton of memory.
## Stop sign
A stop sign is a byte that signifies a "stop" of an object(?) currently being stored in the memory. One way to look at it is to see it is to imagine textbooks being stored as only unordered pages. How do we know where one book ends and the other begins? We need a divider that splits these pages and a "label" after the dividers to clarify which pages belong to which book.