# Introduction
This cheat sheet contains a bunch of commonly used Linux commands for quick reference. The description of the commands both include formal definitions and laypeople definitions (refer to [[#`cd [path]`]] for example)
# Keywords
A list of keywords will be provided just in case you don't remember the formal terminology (I mean I fuckin' don't).
- Directory / folder / room
- 
# List
## Directory-related commands
## File-manipulation commands
#### `touch [filename]`
Creates an empty file
## Listing/reading commands
#### `ls` - Long list (details)

## Important flags
### Human-readable format
Have you ever wondered what `20101023B` is in GB? Do `-h` for your command. Now it'll show `20.1G`.
### Recursive listing
Do `-R` or `-r` depending on the command to recursively apply the command to the inner directories of the current one.
### Sort by size
Do `-S` to sort output by size, biggest to smallest.
Do `-r` to sort in reverse order.
### Sort by time
Do `-t` to sort output by time, latest to earliest.
### Show full time
Do `--full-time` to show the full time from microsecond time.
## `cd [path]`
Change current working directory to specified one. In other words, move to specified folder