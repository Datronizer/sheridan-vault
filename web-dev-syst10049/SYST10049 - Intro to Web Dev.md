This course focuses on simple web development, using HTML and CSS to set up, design, and deploy the website. 

The course is split into 2 sections: 
- Section 1 from **Week 1 - Week 6**, focusing on [[Hypertext Markup Language|HTML]].
- Section 2 from **Week 8 - Week 13**, focusing on [[CSS]].
**Week 7** and **Week 14** are reserved for **Midterm** and **Finals**

There will be 5 quizzes, all monitored using [[Lockdown Browser]].

# Evaluations
**Assignments:** 4 total * 10% grade = 40% grade
**Quizzes:** 5 total * 2% grade = 10% grade
**Exams:** 
- Midterm Exam: 25%
- Final Exam: 25%
# Passing grade
Follows the [[Sheridan College#50/50 rule|50/50 rule]].

Detailed course description can be found here: https://ulysses.sheridanc.on.ca/coutline/coutlineview.jsp?print=true&courseCode=10049&subjectCode=SYST&version=2023050800&appver=sal&d=null&s=null
# Standard file organization
## Relative path
You should organize your files in hierarchichal order.
An example would be:

public_html
-> syst_10049
->-> index.html
->-> project_1
->->-> something.html
->-> project_2
->->-> sth.html
etc...

Finding a file relies on  `<a href="path/to/file.html">Link label</a>`
This path is called the relative path. You navigate down by typing the file and folder you want. Go up with `../path/to/file`. Go to file in current folder either with `/path/to/file` or `./path/to/file`

Since HTML searches for these files using paths, it is **highly recommended** that you have a logical, hierarchical system for an easier, more organized site.

Also, do use relative paths in your site since submitting assignments will have the interpreter look for the relative file in the submitted assignments rather than your drive. 
## Absolute path
Example: `http://www.apache.org/foundation/FAQ.html`
This is an absolute path. From this link, you go directly to the file, no circular referencing or folder navigation. It's a straightshot to FAQ.html, passing through a supposed "folder" called `foundation`.
# Uploading your work
You are to upload your work to <a href="https://tech.fast.sheridanc.on.ca/services/lamp">cPanel</a>. Go there and use it as you would with your uYeti work repository. This is your cloud VM and you can store your files to make a website here.

Login:
> [!username]- truonchi
> [!password]- redacted
# Lectures
[[web-dev-syst10049/Lectures/Lecture 2|Lecture 2]]
[[web-dev-syst10049/Lectures/Lecture 3|Lecture 3]]
[[Lecture 4 (I skipped last week)]]