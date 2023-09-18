#lecture 
Lecture 1 was used to describe course contents. This is the actual lecture.
# [Progressive Enhancement](https://slate.sheridancollege.ca/d2l/le/content/1141756/viewContent/14861696/View)
A methodology that ensures a web application/site is accessible to everyone, regardless of what kind of device they're using. We do this by separating out application's structure and content from the styling and from the functionality essentially dividing up the development of the site into 3 parts.
## Content/Structure
Define the content of the page and use HTML to add the content and structure of the page/app/document/etc. The content and structure should be viewable/readable in any browsers on any device, including screen readers.
## Styling
Add the CSS styling and layout, ensuring that all browsers/devices are still supported, and add some features of the primary browser/device set. Yes it should still be viewable/readable on all devices and browsers
## Functionality
Add JS functionality, interactivity, and enhancements to all pages. Of course, like the others, this should be supported on all devices/browsers. The Javascript functionality should not be mandatory in order to use the site/application. There **should** be alternatives available for users who can't use the JS functionality.
# Advantages of Progressive Enhancements
## Accessibility
The first clearest advantage is accessibility. PE ensures you develop an accessible site that separates the content from the styling from the function, so that the page can still be used without the layers before it.

Example: Most screen readers don't support JS, but you know the site is still usable before you add the functionality layer
## Portability
Portability means you can take your program and run it on **any** machine. PE ensures the app is usable in the browser, even when the user is using an assistive device like screen readers.
## Modularity
Think of the program as a LEGO house. The house is built with many LEGO bricks and each brick is different, but some of these brick designs can be reused in other houses or different parts of the same house. In PE, you end up creating modular components that can be used in different applications without needing modification.
## Performance
Using PE approach will allow faster load times by putting JS, CSS, and other files in cache so that the browsers don't have to re-request them every single time you reload.

You can view this in Inspect -> Storage
## 
To sum up, it is important that you get the content done first. Don't worry too much about CSS or JS. The point is to have the site be accessible anywhere and everywhere.

# Accessible Web Design Development
[Web Content Accessibility Guidelines](https://www.w3.org/TR/WCAG22/) (WCAG), developed through the World Wide Web Consortium's (W3C's) Web Accessibility Initiative (WAI) defines the standards fro making web content accessible to people with disabilities.

There are 4 principles (POUR):
1. **P**erceivable: All users must be able to receive (hear, read, etc.) and interpret ***content***
2. **O**perable: All users should be able to ***use*** the site/app effectively
3. **U**nderstandable: All users should be able to comprehend the meaning of ***content***
4. **R**obust: All users with any agent (i.e. browser) should be able to use the site without it crashing.

There are 3 levels of conformance: **A, AA, AAA**. In order for a Wen page to conform to WCAG 2.2, it must meet at least one level of the conformance.
- Level A (minimum): satisfy all 32 criteria (25 from 2.0, 5 from 2.1, 2 from 2.2). These are the easiest ones to pass and don't require a lot of extra coding.
- Level AA: requires level A conformance + 24 extra success criteria (13 from 2.0, 7 from 2.1, 4 from 2.2). There are usually more work to implement and **many** websites fail this criteria.
- Level AAA: "nice to have" criteria that isn't required for conformance. These criteria are usually very specific, addressing specific needs and/or dealing with uncommon content.