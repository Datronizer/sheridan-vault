---
tags:
  - concept
aliases:
  - American Standard Code for Information Interchange
  - ASCII
  - ISO-IR-006
  - ANSI_X3.4-1968
  - ANSI_X3.4-1986
  - ISO_646.irv:1991
  - ISO646-US
  - us
  - IBM367
  - cp367
---

The American Standard Code for Information Interchange (ASCII) is a system of [[Encoding]] that translates binary into characters based on their patters.
# ASCII Table
The ASCII table is a table of all characters supported in ASCII, for example, pi. Here's how you can type these characters into your text editor.
- Look up the ASCII number of the symbol
- Hold Alt and type that number
- The new symbol should appear

For the full table from the official ASCII devs, go to [https://asciitable.com](https://asciitable.com).
# History
Now that we know how memory allocation works, we can discuss the formation of the ASCII table. The ASCII table was formed from a need for a unified memory organization system for characters in a computer. 

Suppose you [[Memory & Compiler Maps|allocate]] A = 65, B = 66, etc. and your PC allocates A = 42, B = 43, etc. If I send an email to you, the contents inside my email, which is [[Lecture 2 - TELE13167#The 5 TCP/IP layers|converted from letters to numbers]] to be sent, to your inbox, to letters again, will be jumbled because we have different addresses for our characters. This got annoying fast, so computer scientists eventually got together to address the issue and form the ASCII table.

This was fine for a while until we realized we need to accommodate all the other languages like Arabic, Chinese, Hebrew, etc. We then realized we needed way more than 99 letters. So we did the simplest thing: we combined 2 bytes into the new standard. Guess what that's called.

That's right, we made [[Unicode]], but that's a separate topic.

Eventually we realized we kind of don't need the entirety of Unicode for coding purposes, so we made another replacement. Say hello to [[UTF-8]]. 
# How it works
Scientists agreed on a system called the ASCII Table where each individual character is assigned a "pattern" the size of 1 byte. 

When the user types a character on the keyboard, the encoding of the character gets blasted through the input into the CPU where it reads this pattern. It realises this pattern matches a specific character and outputs that thing back.