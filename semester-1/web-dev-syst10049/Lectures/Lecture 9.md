I'll pretend I know what's going on here

# `display: grid`
Yo guess what this does. Yes genius, it will display items in a grid. How? So we know everthing is a box right? Now assume all these boxes are just cells on a table, and the table is the viewport of the browser.

Now we can build elements in a "griddy" way (don't ever say that again).

First, name your elements. Give your elements a name using `grid-area: "some-name"`.
Second, sort your elements in a table-y format like so:
```
main {
grid-template-areas:
	"nav" "body" "aside"
	"nav" "footer" "footer"
	"nav" "x" "x"
}

div.body {
	grid-area: "body"
}

nav {
	grid-area: "nav"
}

aside {
	grid-area: "aside"
}

footer {
	grid-area: "footer"
}

div {
	grid-area: "x"
}
```
Of course if you have other width settings in the individual elements, they would override the automatic width set by the grid. Evidently, this means we can override the height and width of the elements as we please. We can do this using `grid-templaate-columns` and `grid-templaate-rows`.

```
<!-- The below grid has 3 rows and 4 columns -->

main {
	grid-template-areas:
		"nav" "body" "aside" "aside"
		"nav" "footer" "aside" "aside"
		"nav" "x" "x" "x"
	grid-template-columns: 1fr 3fr 1fr 1fr
	grid-template-rows: 2fr 2fr 1fr
}
```
The above code will grow the 2nd column by 3 times its starting width, and the first 2 rows by double its height.