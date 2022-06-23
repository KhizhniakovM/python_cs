# Analyzing Algorithms Part III
# In this lesson, we will work out a generalization for the number of instructions executed for an
# array of length n

# Let's try to generalize the running time for an array of size n.

# ../images/007.png

# If we use the above formulas and apply an array of size 5 to them, then the cost should match
# with what we calculated earlier.

# Total Cost= Outer loop instructions + Inner loop instructions

# =[2*(n+1)+2n]+[2n+7[\frac{n*(n-1)}{2}]]

# =[2*(5+1)+10]+[10+7[\frac{5*(5-1)}{2}]]

# =[12+10]+[10+7[\frac{5*4}{2}]]

# =22+[10+7*10]

# =22+10+70

# =102 instructions

# ? Summation of Series
# We glossed over how we converted the sum of the series 0 + 1 + 2 ...(n-1) to n(n-1)⁄2? However,
# even though we promised to steer clear of complicated mathematics as much as possible, this is one
# of the cardinal summations that you must know. Without a formal proof, remember that the sum of
# the first k natural numbers can be represented as:

# 1+2+3+4⋯k
# =\frac{k*(k+1)}{2}

# If you add the first 5 natural numbers the sum is:
# ../images/008.png

# Coming across this summation is very common in algorithmic analysis and, without getting
# too technical, if you can identify this series, then you know how to apply a formula to sum it up.

# ? Running Time as n Increases
# As the size of the array increases, so does the number of instructions executed. Below is a
# table that shows the instructions executed for the worst case as the size of the array increases.

# ../images/009.png
# ../images/010.png

# The intention of doing the dry run and accounting for each line of code executed is to instill in
# the reader that the instruction count varies with the input size. Calculating down to this detail
# is often not necessary and with experience one can correctly recognize the complexity of various
# code snippets. As you'll learn in the next chapters, we reason about algorithm complexity in a ballpark
# sense, and calculating exact instruction counts is almost always unnecessary.
