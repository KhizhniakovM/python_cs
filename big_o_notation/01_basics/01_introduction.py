# Introduction
# This chapter lays the groundwork for the material covered in the course and sets out the expectations 
# for the readers.

# ? The Interview Room
# You're in an interview room, and you've just completed white-boarding the interviewer's question. 
# Inside, you feel ecstatic; It's your dream company and you nailed the question. However, just when 
# you think the coast is clear, the interviewer follows up with a question on the time or space 
# complexity of your solution. The blank drawn across your face gives away your ineptness at analyzing 
# algorithm complexity in space or time. In this common interview situation, most computer science 
# graduates are still able to muster up a reasonable answer. For candidates lacking the formal education, 
# however, reasoning about algorithms in terms of the big Oh notation becomes a big uh oh!.

# The intended readership of this course includes folks who are graduates of boot-camps, career-switchers 
# into programming jobs or just established industry veterans who want a quick revision on the 
# topic of complexity theory. The course uses layman's terms to describe the concepts commonly 
# used in the industry while intentionally avoiding the intricate mathematical gymnastics often 
# involved in analyzing algorithms so that the subject material is comprehensible for readers at all 
# skill levels. At the same time, this course may not deliver great value to individuals who already 
# have a firm grasp of algorithms and data-structures or to those that hold a degree in computer science.

# ? Why does complexity matter?
# If you are working on a class assignment or a customer application with a few dozen users, you can 
# take the liberty to ignore the space and time complexity of your solution. However, the moment you 
# step into the professional world and write software with strict SLAs (service level agreements) or 
# for millions of users, your choice of algorithm and data-structures starts to matter. A well designed 
# and thought out software will scale elegantly and set itself apart from poorly written competitors.

# Usually, the 101 example used to teach complexity is sorting of integers. Below are three example 
# programs that sort integers using different sorting algorithms.

# The code implementations above run on datasets of 5000 elements. Below are some crude tests (run on a Macbook) 
# for the three algorithms. All times are in milliseconds

# ../images/001.png

# The results tabulated above should provide plenty of motivation for software developers to increase 
# their understanding of algorithmic performance. Bubble sort progressively degrades in performance 
# as the input size increases, whereas the other two algorithms perform roughly the same. We'll have 
# more to say about their performances in the next chapter.

# ? Time & Space
# The astute reader would notice the use of an additional array in the merge sort code, named scratch 
# array. This is the classic trade-off in the computer science realm. Throwing more space at a problem 
# allows us to bring down the execution time, and vice versa. Generally, time and space have an inversely 
# proportional relationship with each other; if space increases then execution time decreases, and if 
# execution time increases then space decreases.
