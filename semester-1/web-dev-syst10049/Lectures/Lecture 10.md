# Media queries
Media quesries are used to change the layout of a page by querying for elements we wish to change. Syntax is simple:
```
@media screen and (min-width: 750px)
{
	h1 {
		color: red
	}
}
```
This changes the color of `h1` to `red` when the screen size is greater than 750px. Else (0 - 749px), the color goes to default.

Using this in addition to a grid display will allow for a responsive page with minimal editing between different screen sizes.

You can set this up using three ways:
1. Use embedded style elements: Keep it in the `<style>` tags
2. Link to an external stylesheet:, must specify the media type and conditions (`media="logic media and (expression / conditions)"`)
	- Example:
		- `<link rel="stylesheet" media="screen" href="desktop.css"`
		- `<link rel="stylesheet" media="screen and (min-width: 481px) and (max-width: 768px)" href="tablet.css"`
		- `<link rel="stylesheet" media="screen and (min-width: 0px) and (max-width: 480px)" href="mobile.css"`
		- `<link rel="stylesheet" media="print" href="print.css"`
		- In this order, the `desktop.css` stylesheet would be loaded first as a default for any styles not changed in subsequent stylesheets.

3. Call an external stylesheet using `@import`:
	- This allows multiple `.css` files to be imported in the one `.css` file (e.g. `main.css`) then linked in the html page. The only requirement is that any `@import` rules need to come before the rest of the style rules.
	- Example:
		- `@import url("tablet.css") screen and (min-width: 481px) and (max-width: 768px);`
		- `@import url("mobile.css") screen and (min-width: 0px) and (max-width: 480px);`
		- We import all these in one `.css` file, let's say `basis.css`. Then all we have to do is link `basis.css` in the main `.html` file, and `basis.css` will automatically import the other 3 `.css` files. It's kinda like importing an entire folder.