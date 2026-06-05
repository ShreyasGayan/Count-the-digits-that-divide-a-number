Count the Digits That Divide a Number
A Python solution for LeetCode Problem 2520: "Count the Digits That Divide a Number".


Problem Description
Given an integer num, return the number of digits in num that divide num.
An integer val divides nums if nums % val == 0.

Examples
Example 1:Input: num = 7
Output: 1
Explanation: 7 divides itself, hence the answer is 1.

Example 2:Input: num = 121
Output: 2
Explanation: 121 is divisible by 1, but not 2. Since 1 occurs twice as a digit, we return 2.

Example 3:Input: num = 1248
Output: 4
Explanation: 1248 is divisible by all of its digits, hence the answer is 4.

Constraints1 <= num <= 10^9
num does not contain 0 as one of its digits.


Solution Approach
The solution converts the integer into a string to easily iterate through each individual digit. For each digit character, it converts the character back into an integer and checks if it can divide the original number without leaving a remainder (num % int(i) == 0). A counter keeps track of the valid dividing digits and returns the total.Code Structurepythonclass Solution(object):


How to Run
Clone this repository.
Ensure you have Python installed.
Import the class and call the method with an integer:
pythonsol = Solution()
print(sol.countDigits(121))  # Output: 2
