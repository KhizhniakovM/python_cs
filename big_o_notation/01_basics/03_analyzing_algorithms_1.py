# Analyzing Algorithms
# We start our journey into the world of complexity by analyzing the insertion sort algorithm.

# Insertion Sort Analysis
# Let's start with the example of an array that contains 5 elements sorted in the worst possible order,
# i.e. descending when we want to sort the array in an ascending order. We'll use the insertion sort
# algorithm as the guinea pig for our analysis.

# ../images/002.png

# We'll not delve into explaining the algorithm itself as our focus is on analyzing algorithm performance.
# The coursework assumes that readers have an understanding of the fundamental algorithms used in
# everyday computing tasks, or they can do a quick web-search to get up to speed on the algorithm
# under discussion. Let's proceed with the implementation of the algorithm first:

# class Demonstration {
#     static void insertionSort(int[] input) {
#         for (int i = 0; i < input.length; i++) {
#             int key = input[i];
#             int j = i - 1;
#             while (j >= 0 && input[j] > key) {
#                 if(input[j] > key){
#                     int tmp = input[j];
#                     input[j] = key;
#                     input[j + 1] = tmp;
#                     j--;
#                 }
#             }
#         }
#     }

#     static void printArray(int[] input) {
#         System.out.println();
#         for (int i = 0; i < input.length; i++)
#             System.out.print(" " + input[i] + " ");
#         System.out.println();
#     }

#     public static void main( String args[] ) {
#         int[] input = new int[] {7, 6, 5, 4, 3, 2, 1};
#         insertionSort(input);
#         printArray(input);
#     }
# }

# Below, we extract out the meat of the algorithm.

# 1.         for (int i = 0; i < input.length; i++) {
# 2.             int key = input[i];
# 3.             j = i - 1;
# 4.             while (j >= 0 && input[j] > key) {
# 5.                 if (input[j] > key) {
# 6.                     int tmp = input[j];
# 7.                     input[j] = key;
# 8.                     input[j + 1] = tmp;
# 9.                     j--;
# 10.                 }
# 11.            }
# 12.        }

# ? Analyzing the program
# For simplicity, let's assume that each code statement gets executed as a single machine instruction
# and we measure the total cost of running the program in terms of total number of instructions
# executed. This gives us a simple formula to measure the running time of our program expressed below:

# ? Running Time = Instructions executed in For loop + Instructions executed in While loop

# ? Analyzing the outer for loop
# Let's start with the outer for loop and see how many instructions would get executed for each
# iteration of the outer loop. For now, forget about the inner while loop; we'll analyze it separately
# from the outer for loop.

# ../images/003.png
# ../images/004.png

# ? Analyzing the inner while loop
# ../images/005.png

# Note that with the above analysis, we got a handle on the number of instructions that get executed
# per iteration of each loop given an input size of n. We can compute the instruction count for all
# iterations and sum them up to get the execution count for the entire run. In later sections, we'll
# compute a generalization that'll allow us to count the number of executions for the entire algorithm
# with a single formula.

# It is also important to be cognizant that we are considering each line of code as a machine instruction,
# which isn't true. A line of code may result in several individual machine instructions; however,
# this shouldn't affect our analysis as long as we maintain the same yardstick when performing analysis
# across algorithms. Think of it as expressing the speed of an athlete in km/hour, miles/hour,
# centimeters/minutes etc. Whichever metric you choose for your representation, it will not affect
# the speed with which the athlete runs.
