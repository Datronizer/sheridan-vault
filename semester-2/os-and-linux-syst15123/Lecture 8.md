# Regular Expressions
A search method where you "describe" what you're looking for. 

## grep
grep is a famliy of commands in Linux that is used to search for a RegEx string. It includes grep, egrep, and fgrep
### grep
Syntax: `grep [options]... REGEX file/s`

Some common `options`: 
- `-i` Case insensitive search (default is case sensitive)
- `-w` (Whole word search) Select only lines containing matches that form **whole words**
- `-n` Shows line numbers upon search (prefixed to search results).
### egrep
Same as using `grep -E`, interprets **patterns** as extended regular expressions. Uses a ton of computing power.
### fgrep
Interprets **patterns** as fixed strings, not regular expressions. This is more suitable for searching for a very specific string you already know beforehand. Extremely fast and optimal.
## BRE (Basic RegEx)
- `\`: Escape sequence. Matches a char that is a RegEx special char.
- `.`: **Any** single char.
- `^`: Starting anchor. Returns only lines that starts with the specified character. 
- `$`: Ending anchor. Returns only lines that ends with the specified character.
	- If you want to find empty lines, do `grep '^$' filename`
	- This returns a line that starts with nothing and ends with nothing => empty.
- `*`: Repeat pattern. Returns only lines that repeats the char before the `*`. 
	- The number of repetitions range from 0 to FUCKING INFINITY. 
	- Meaning ANY repetitions, with or without the specified repeating char itself, will be returned
- `{min,max}`: Same as `*` but has a limit.
	- The number of repetitions range from `min` to `max`, both inclusive.
	- Not specifying `max` after writing a comma means go from `min` to infinity
	- Not specifying `max` (only specifying `min`, no comma) means find only substrings that repeat `min` times
	- `{0,}` means the same thing as `*`
	- If it doesn't work, check if you're using `grep` and forgot `\` for the braces
- `[]` works the same as [[Linux globbing]]

Example:
- `grep -niwE '[0-9]{2,3}' /etc/hosts` finds every substring with 2-3 numbers in `/etc/hosts`
- `grep -niwE '^1e$' /etc/hosts` finds every substring that STARTS with `1`, and ENDS with `e`, with NOTHING in between them.
- But `grep -niwE '^1.*e$' /etc/hosts` finds every substring that STARTS with `1`, and ENDS with `e`, with any chars in between them

There are some preset set of characters you can use to ease your search efforts. They will not be covered here. Please refer to `man`.

### ERE (Extended RegEx)
`?`: Same as `{0,1}`. Returns an optional character.
`+`: Same as `{1,}`. Returns a character repeated one or more times.
`|`: OR operator. Finds EVERYTHING thats matches the ENTIRE LEFT SIDE or THE ENTIRE RIGHT SIDE.
`()`: Grouping. Groups things together to limit the reach of the search parameter.

Example:
- `grep stev|phen` searches for all `stev` and `phen`'s.
- `grep ste(v|ph)en` searches for all substrings that's either `steven` or `stephen`.

# `sed` command
`sed` is a stream editor for filtering and transforming text. It's used to perform basic text transformations on an input stream (a file or input from a pipeline).

Guess what? THIS WORKS WITH REGEX!

## `sed` special characters
`/` (forward slash) is used to separate characters in `sed`.

## How it works
Reads from input, one line at a time, and edits the stream based on set commands.

`d` removes an entire line that contains a specified value.
`s` substitutes a substring with another specified substring.
To remove a substring, it's better to just substitute that string with a different one.
But to remove a line, just use delete.
### Substitution
Syntax for substitution:
Always start by piping into `sed -e`.
Then use this:
`[address1[,address2]]s/pattern/replacement/[flags]` (what the fuck)

Example:
- `echo "hello there" | sed -e 's/e/E/'` replaces the first `e` with `E`
- `echo "hello there" | sed -e 's/e/E/3'` replaces only the third `e` with `E`
- `echo "hello there" | sed -e 's/e/E/g'` replaces every `e` with `E`
- `echo "hello there" | sed -e 's/e/E/1' -e 's/e/E/2` replaces only the first and third `e` with `E`
	- The reason it's like that is because `sed` runs through the whole line FIRST. Then it pipes that edited line into its own output and runs it again. Once all of it's done it goes down to the next line.

Suppose you're trying to substitute a file that has a bunch of slashes. It will certainly not work since `/` is reserved for `sed`. HOWEVER, WE HAVE AN ALTERNATE OPTION, TECHNICALLY WE HAVE 5: `/`, `@`, `:`, `;`, `,`.
### Delete
For delete, please refer to the slides for more information and examples. I can't take notes fast enough, this man is blazing through.
### Backreferences
Re-use a part of RegEx selected by grouping (what the fuck).

Example:
Suppose I have a file `f` with the contents: 
```
aaaa
abab
abcd
1c1c
```

If I do `sed 's/\([a-z]\)\1\1\1/XXXX/g' f`, I'll get
```
XXXX
abab
abcd
1c1c
```

How this works:
1. I specify a RegEx, here it's to find an alpha char.
2. Then I say, "hey, for the next character, follow my instructions for the 1st character"
3. Then I say, "good, now do that for the next one"
4. "And the next one."
5. Once you've found all 4 characters matching my specifications, replace them with XXXX.
6. To this for all the chars you find on the line

Next, do `sed 's/\([0-9a-z]\)\([a-z]\)\1\2/XXXX/g' f` to get
```
XXXX
XXXX
abcd
XXXX
```

How this works:
1. I specify a RegEx for the 1st character
2. Now I specify a RegEx for the 2nd character
3. Now for the 3rd character, I want to backreference my search parameters to the first one (basically saying, "hey for the third character, use the same pattern I provided for the first one).
4. Same as above but for 2nd and 4th.
5. So on
6. and so forth.

Else, do `sed 's/\([0-9a-z][a-z]\)\1/XXXX/g' f` to get the same as the immediate one preceding this.

This method just groups the first 2 characters and search only once instead of thrice.

# `awk` command
AWK is a pattern scanning and processing language designed for processing text-based data, either in files, data streams, or in pipes.

Very powerful in companies, sometimes they'd hire a person that specializes in this because it's a very useful knowledge.

## Print text file with awk
`awk '{print}' filename` OR `awk '{print $0}' filename`
This works the same as `cat filename`.

The `$0` is the field we want to print. 0 is the whole line, 1 is the first field, and so on.
But how do we print a field? We'll need a delimiter that cuts the field for us.

`awk -F[delimiter] '{print $[fieldNum]}' filename` should do the trick.

Pattern matching is also supported for this.
`awk -F: '$3<=10{print $0}' /etc/passwd` means to print the whole line where the 3rd field, delimited by `:`, is less than or equal 10

Printing lines can also be done with the `NR` variable
`awk 'NR==10 {print $0}' filename` prints line 10 of some file.

## awk arithmetic
Sometimes you want a rule to run before or after all the lines have been read. To do that, use BEGIN or END accordingly before a rule you wish to execute.

awk can compute floating point numbers, whereas bash can't. Here's how
`awk 'BEGIN {printf "%.3f\n", 2005.50/3}'`

This prints the result of `2005.50 / 3` at the beginning before any lines are read.

Here's a fun one. This command will show you your top 10 most used commands:
```
$ history | awk '{print $2}' | sort | uniq -c | sort -rn | head -n 10
     87 ls
     55 rm
     52 cd
     51 tree
     41 mkdir
     34 grep
     31 echo
     29 touch
     22 chmod
     21 man
```

## Running commands from files
You can create a file, say `p.awk`, the extension only serves to clarify what it does, it's not necessary.

Now run the previous top 10 command again using the file. You'd get this:
```
$ history | awk -f p.awk | sort | uniq -c | sort -rn | head -n 10
     87 ls
     55 rm
     52 cd
     51 tree
     41 mkdir
     34 grep
     31 echo
     29 touch
     22 chmod
     21 man
```

# Backup and Restore data
There are 3 types of backups:
- Full backup: Copies EVERYTHING into a restore media.
	- Pros: Copies everything so no data will be lost
	- Cons: Slow as shit, heavy as shit
- Incremental backup: Copies only the data that's been changed the day before.
	- Pros: Much smaller, much faster
	- Cons: Data recovery is a bitchhhhhhh. You'll have to incrementally restore your data in the order they were taken.
- Differential backup: Copies the data that's been changed since the full backup
	- Pros: Safer than incremental, easier to recover data
	- Cons: By the end of the week, your backup will be equal to the full backup. Might as well do a full backup at that point.

Incremental creates a snapshot, checks that against the previous snapshot (if available), and updates the archive based on the difference between the snapshots.