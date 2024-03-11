# Garbage collection
## Introduction
Recall the concept of [[Memory & Compiler Maps]]. When we declare a variable, we allocate some memory to this number. But what if we don't need to use it again?

Clearly, human nature would compel us to throw away what we don't need. How do computers do this? In Java, we rely on a runtime process known as **garbage collection**. 

The garbage collector would (ideally) go into the memory, check if a variable is used, and if not, disposes of it and free up some memory. How does it know? 

In the machine code level, each of these variables are marked with a flag that tells us if it's being used or not, and the garbage collector can read these to throw them away. That's the ideal scenario. 

> [!note] Entropy and its effects on computers 
> Computers naturally compounds errors and inefficiencies over time due to entropy. These will build up and eventually overwhelms the garbage collector. It could be a matter of hours or years based on use case and code quality. 
> 
> This is why you should restart your computers every now and then, including servers! Servers do get restarted occasionally during "maintenance times".


