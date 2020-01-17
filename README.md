# Mortgage Calculator
A python learning project to calculate information about a mortgage.

## About this Project

This was one of the first projects on my journey to learn Python. Someone I know was in the process of buying a house, so I decided to build a mortgage calculator that can calculate various values relevent to a mortgage. I also wanted this program to be able to calculate how much money can be saved in interest by paying an extra amount each month. 

This project is very simple and needs to be run in the commmand line. Upon launch, the user will be asked some questions about a mortgage then the program creats a .txt file with the results of the calculations.

## Project Learning Goals

Generally, I like to have learning goals in mind for a project. The following are specific things that I wanted to learn while working on the project.

- Become more comfortable writing code in the Python language by creating a simple program that is usable and has a clear function
- Learn how to write data to a text file using the `with` keyword and a context manager

## About the Code

I’m writing this README several months after completing this project, and looking back, I can see how far I’ve come as a programmer. The code above is very simple. The only way to run the program is to navigate to the appropriate directory and running the code in the terminal. There’s no python version number specified, there’s no error handling, and the program probably has floating point rounding errors. The program doesn't even have a single function definition or custom classes. It simply runs the code from top to bottom and hopes the user can provide the correct input.

I did, however, achieve my learning goals. This program uses both a `for` loop and a `while` loop, `if…else` conditional statements, and string formatting. It has a clear purpose, and is functional. There is also a context manager that opens and writes data to a file using the `with` keyword. I didn’t fully understand context managers at the time, but at least I was using them to accomplish tasks in a program.

## Running the Program

Running the program requires navigating to the correct directory in the terminal launching the program with the `python` or `python3` command, depedning on how your environment is set up. Upon launch, the user is asked for input, the program then calculates some values and saves the output to a text file in the same directory.

As an example, we can consider a $350,000 mortgage at 2.95% interest with a term of 15 years. We will be making 1 payment a month with an additional $150 added to each payment. When we launch the program, we simply answer the questions as they are asked:

```
What is the loan amount?
350000
What is the interest rate?
2.95
What is the loan term in years?
15
How many payments will you make each month?
1
How much extra money will you pay each month?
150
```

At this point, the program appears to finish without any indication to the user what has happened, however, the program has created a text file in the current directory called `payment.txt`. When we open the file, we find the output of the program:

>Your monthly payment is 2558.628091815365. 
>Over 180 months, you will pay $433553.05652676575. 
>
>
>For payment 1, $860.4166666666667 goes to interest and $1698.2114251486985 goes to principle. 
>The remaining principle is $348301.7885748513 
>A total of $860.4166666666667 has gone to interest over the life of the loan.
>
>For payment 2, $856.2418969131762 goes to interest and $1702.386194902189 goes to principle. 
>The remaining principle is $346599.4023799491 
>A total of $1716.6585635798428 has gone to interest over the life of the loan.
>
>...
>
>For payment 166, $12.171478960076463 goes to interest and $2546.4566128552888 goes to principle. 
>The remaining principle is $2404.6534725995434 
>A total of $77136.91671395021 has gone to interest over the life of the loan.
>
>Your last payment will be $2410.5649123863504 after 166 payments. 
>A total of $77142.82815373702 has gone to interest over the life of the loan.
>You have saved $6410.228373028731 by paying an additional $150.0 per payment.

The text file contains information for each monthly payment (without any rounding) and a summary at the end. In the first two lines, we see our monthly payment is $2,558.63, and after 180 months (15 years) we will pay  $433,553.06 in total. At the bottom of the file, however, we see our last payment occurs on month 167 (13 years 11 months) because we were paying an extra $150 each month which saves us $6,410.23.

## How to Improve

Probably the best thing I can do to improve my coding skills moving forward is getting feedback from knowledgeable people. Without external feedback, I don’t really know if my code is good or bad, and I don’t really know the best places to focus my efforts. Other than that, here are a few other areas I could improve the program.

- Use custom classes and function definitions to help clean up redundant code
- Use more comments and docstings to explain not only the different parts of the code, but also how the code works
- Make use of name spaces and global variables to better organize monthly data and cumulative data
- Include error handling to deal with silly human behavior