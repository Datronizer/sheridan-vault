# HTML Elements
## Headings and Paragraphs
### `<p>`
Paragraphs! Recommended to use for short paragraphs, anything that looks too wordy should use `<div>` or `<section>` or `<article>` instead. Refer to the "Semantics and Non-Semantics" section.

### `<h1>...<h6>`
These are heading tags, sizes ranging from h1 to h6. Typically, none of these are actually ordered and the values are generally only for screen readers. You should, however, still order them correctly.

`<h1>` has a font size that is twice that of `<p>`, `<h2>` is `1.5em`, etc. 

## Emphasis and Importance
### `<em>`
Short for "emphasis", can change the meaning of the sentence. Recommended for screen readers. Visually, it italicizes text.
### `<strong>`
Visually it boldens text. Used to signify strong importance, seriousness, urgency.
## Italics, bold, and underline
Mostly for appearances, does not affect screen readers. Should no longer be used. Readability is encouraged.
## Image and Multimedia
### `<img>`
The `<img>` tag is used to add a picture to your page. It does not require a closing tag, but it does require a source attribute, for example: `src="https://example.com/hello.jpg"`. 

The `alt` attribute is recommended for accessibility so that screen readers can interpret what the image describes.
### `<video>`
Also requires a source, but as a tag. Example:
``` 
<video>
	<source src="something.mp4">
	Your browser does not support the video tag
</video>
```
The inner text is for when a browser cannot render the video (like a screen reader or a simple web browsing device), then it will show the text instead.
### `<audio>`

# Interactive content
## Absolute and Relative URLs/paths
**A relative path** describes the location of the file relative to the current (working) directory.
**An absolute path** describes the location from the **root** directory.

Example (also make your class folder look like this on cPanel):
![[Pasted image 20230926084108.png]]

To reach a specific file through absolute path, first specify the correct protocol (`http://` or `https://`). Then type the correct domain (in our case it's `https://xxxxx.dev.fast.sheridanc.on.ca`). Now you are in the root folder. To go deeper, type the necessary folder (`/SYST10049/`). Finally, choose the file. If the file is not specified, it automatically opens `index.html`.

You can also use a relative URL to open a page from your directory. In fact it is recommended that you use relative URLs as it is a "safer", more "portable" way to reference a file. Suppose you change your domain. If you used an absolute link, you might have to change **EVERY** `href` in your sites just to fix the references. Development-wise AND use-wise, you should, and I highly recommend, use relative paths. 
<small>Remember what Matt said ( - this message only applies to Chien)</small>

## `<a>` - anchor tag
### Hyperlinks
#### External pages
To create a hyperlink, use the anchor tag `<a>` and add the link you wish to reach into the `href` tag. Example, I want a link on my site that goes to Google. I would do `<a href="https://www.google.com" />`.
#### Internal pages
You can also do anchor links with relative links. E.g.: `<a href="./catPictures.html" />`.
#### New tab
To open link in new tab, do `target="_blank"` for the `target` attribute.
### Bookmarks
You can use anchor tags to "bookmark" your page. What do I mean by that? Suppose I reached the bottom of the page and I want to go to the top. I can create a "bookmark" that "marks" where the top is and it would move me right to the top. This is often used for "go to top" buttons, or to move you to the contact details section of the page. 

Think of it like a hyperlink to a section in the page. You signify the `href` i.e. `href="/#/about-me"` and it will take me to the section with the `id="about-me"`. The `#` sign basically says, "this element is in this page, don't reload, just find that element and move down there." You can also do `href="somesite.com/#/about-me"` and it will go to that site and find an element with that `id`.
### Calling and Emailing
You can turn an `href` into a "call" or "email" button. To force the browser to force your device to initiate a call, do `href="tel:+YOURNUMBER"`. To text an SMS do `href="sms:+YOURNUMBERHERE?&body="Hello%2520world%252C"`. This will send "Hello world!" to the number of your choice. To email, do `href="mailto:your@email.com?subject=Hello World!&body=Your mom"`.