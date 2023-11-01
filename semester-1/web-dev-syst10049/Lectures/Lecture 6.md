# Marking Up Textual Content
## Inline text semantics
### Quotations
#### `<q>`
Quote tags indicates that the enclosed text is a short line quotation. Most browsers would implement this with quotation marks.
#### `<cite>`
Citation tags is used to describe a reference, must include title of that work.
### Definitions
#### `<dfn>`
Definition tags is used to represent the defining instance of a term, often only for the first time this term appears in a document. The nearest parent tag must also contain a definition of this item.
#### `<abbr>`
Abbreviation tags allow a text to be abbreviated and display its full content upon mouse hover. Use the `title` attribute to show the description of the abbreviation.
### Address
#### `<address>`
Address tags are used for contact information. Must only have address/contact information.
### Superscript and Subscript
#### `<sub>` and `<sup>`
Subscript tags, well.... subs a script and brings it down. Superscript is the reverse. It pushes the text up.
### Computer code
#### `<code>`
defines a fragment of computer code. does not preserve extra whitespace and line-breaks.
#### `<var>`
defines a variable. The variable could be a variable in a mathematical expression or a variable in programming context.
#### `<samp>`
represents output from a program or computing system.
#### `<kbd>`
represents user input, like keyboard input or voice commands
### Time and Date
EWWWWWWW I HATE TIME AND DATE FORMATTING
#### `<time>`
represents its contents, along with a machine-readable form of those contents in the datetime attribute. The kind of content is limited to various kinds of dates, times, time-zone offsets, and durations. 
- The datetime attribute may be present. 
	- If present, its value must be a representation of the element's contents in a machine-readable format. 
	- A time element that does not have a datetime content attribute must not have any element descendants.
### Demarcation
#### `<del>` and `<ins>`
Indicates a text has been altered. `<del>` indicates this text is deleted, `<ins>` indicates the deleted text has been replaced with this new text.
## Block text semantics
### Block quotes and poems
#### `<pre>`
Preformatted text, white space and line breaks preserved.
#### `<blockquote>`
Specifies a section quoted from another source. For short quotations, use the inline quotation [[#`<q>`|<q>]] instead
### Non-semantic wrappers
#### `<div>`

#### `<span>`

### Empty elements
#### `<br>` and `<hr>`
Breaks line to jump down / draws a horizontal line across the page.
#### `<img>`
Adds an image using attribute `src`
