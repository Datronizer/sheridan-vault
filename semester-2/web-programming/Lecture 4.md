# DOM Tree
The **D**ocument **O**bject **M**odel (**DOM**) is a way to model (get it?) the structure of an HTML file. The DOM is constructed as a **tree** of objects--of course the objects being the tags within the page.

Evidently, this being a tree means there is a root and there are branches. The root in this case is the `<html>` tag. Every direct child of the root is a branch. And everything within each of those child is a family of that child, who--in this case--are the parents.

JS allows this tree structure to be dynamic. We can change the elements around in the tree and make them do things. That's the power of JS (God I hate this language).
# DOM methods
A webpage is considered a web document. Meaning if we want to do things to the web page (a.k.a. the DOM), we need to reference a class called `document` (at least the names aren't equally stupid).

Here are a few common methods:
## Get methods
### `getElementById('element')`
To grab some element with the `id="someParagraph"`. Say I want to change inner HTML contents of the paragraph, regardless of whatever it is, to "haha stupid" upon the click of a button. I can do this:
```
<script>
	function stupify()
	{
	    document.getElementById("someParagraph").innerHTML = "haha stupid";
	}
</script>

...
<p id="someParagraph">Lorem ipsum dolor sit amet</p>
<button onclick="stupify()">Click me</button>
...
```

### `getElementsByTagName('tagName')`
To grab all elements matching a tagName, say `div`. Do `document.getElementsByTagName("div")`. This will return an [[Intermediate Datatypes#Lists (Arrays)|array]] of elements.

Pay attention to the name of the method, it's actually plural. It's a little unclear but remember 1 thing: there is only **ONE** method that grabs a single element.


