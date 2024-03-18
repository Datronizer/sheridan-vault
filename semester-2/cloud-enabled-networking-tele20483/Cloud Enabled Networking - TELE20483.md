> [!important] This class is ridiculously hard. Very high failure rate. All grades will be strict. Please pay attention and take good notes. Good night and good luck! 

According to professor Ida Leung, half the class fails. To be honest, 50/50 is a good rate, we take those. To up our chances, professor Leung will provide bonus marks. These marks will be provided as such:
- 3 marks max for **attendance**
- 2 marks max for **finishing 75 of quizzes and assignments**

Late submissions will be deducted $(0.9)^d | \text{d being number of days late}$. 
All exams are in person. Test 1 is written only. Test 2 and 3 are both written (65%) and practice (35%).

The **class plan** will be attached in the root folder of this class. Click on "show in Explorer" to reveal it.
The **textbook** will be attached in the textbook folder.

If you want an AWS certification by the end of the class, you can consult [this book](https://www.amazon.ca/Certified-Solutions-Architect-Study-Guide/dp/1119713080). Of course, there will be a ["free" version](https://library.lol/main/B737706D838FA0EEACAE942B2CA7E609) but do make sure to access using Tor. Trust me. Anyways, if you want a physical copy, look up the ISBN: 978-1119713081.

# Lectures
[[semester-2/cloud-enabled-networking-tele20483/lectures/week 1/Cloud Computing Models]]
[[semester-2/cloud-enabled-networking-tele20483/lectures/week 2/Lecture 2|Lecture 2]]
One of these is skipped due to an exam on that day
[[semester-2/cloud-enabled-networking-tele20483/lectures/week 3/Lecture 4|Lecture 4]]
[[semester-2/cloud-enabled-networking-tele20483/lectures/week 4/Lecture 5|Lecture 5]]
[[semester-2/cloud-enabled-networking-tele20483/lectures/week 6/Lecture 6|Lecture 6]]
[[semester-2/cloud-enabled-networking-tele20483/lectures/week 7/Lecture 7|Lecture 7]]
[[semester-2/cloud-enabled-networking-tele20483/lectures/week 8/Lecture 8|Lecture 8]]


# Scaling
## Vertical scaling
Used for applications that need a lot of bandwidth. 
- **Scaling up** means adding more capacity to an existing resource. That or changing the instance type, exmaple: changing a server from **T**iny size to e**X**tra size.
- **Scaling down**: the reverse lol. Dropping capacity due to excess storage for example.
## Horizontal scaling
Web servers will use horizontal scaling because they don't need bandwidth, they need instances instead. Think microservices. You don't need a "bigger" CPU, you just need more instances to independently process requests.

AWS can usually do auto-scaling for your use case. They don't automatically vertically scale your server though. That has to be done manually, because, you know, it requires physical hardware??