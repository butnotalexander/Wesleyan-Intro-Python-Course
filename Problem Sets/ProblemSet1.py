""" 
Problem 1_1:
  Write a function problem1_1() that prints "Problem Set 1". 
  
  Remember that you can execute just the code between the #%% signs by clicking somewhere in that space and the using Ctrl-Enter (Cmd-Enter on Mac).
"""
#%%
def problem1_1():
  print("Problem Set 1")

#%%
"""
Problem 1_2:
Write a function problem1_2(x,y) that prints the sum and product of the numbers x and y on separate lines, the sum printing first.
  >>>problem1_2(3,5)
  8
  15
"""
#%%
def problem1_2(x,y):
  print(x + y)
  print(x * y)

#%% 
"""
Problem 1_3:  
  Write a function problem1_3(n) that adds up the numbers 1 through n and prints out the result. You should use either a 'while' loop or a 'for' loop. Be sure that you check your answer on several numbers n. Be careful that your loop steps through all the numbers from 1 through and including n.

  >>>problem1_3(6)
  21
"""
#%%
def problem1_3(n):
  my_sum = 0
  i = 0
  while i < (n + 1):
    my_sum += i
    i += 1
  print(my_sum)

#%%
"""
Problem 1_4:
  Write a function 'problem1_4(miles)' to convert miles to feet. There are5280 feet in each mile. Make the print out a statement as follows: "There are 10560 feet in 2 miles."  Except for the numbers this state should be exactly as written
  >>>problem1_4(5)
  There are 26400 feet in 5 miles.
"""
#%%
def problem1_4(miles):
  print("There are", miles * 5280, "feet in", miles, "miles.")

#%%
"""
Problem 1_5:
  Write a function 'problem1_5(age)'. This function should use if-elif-else statement to print out "Have a glass of milk." for anyone under 7; "Have a coke." for anyone under 21, and "Have a martini." for anyone 21 or older.

  >>>problem1_5(5)
  Have a glass of milk.

  >>>problem1_5(10)
  Have a coke.

  >>>problem1_5(25)
  Have a martini.
"""
#%%
def problem1_5(age):
  if age < 7:
    print("Have a glass of milk.")
  elif age < 21:
    print("Have a coke.")
  else:
    print("Have a martini.")

#%%
"""
Problem 1_6:
  Write a function 'problem1_6()' that prints the odd numbers from 1 through 100. Make all of these numbers appear on the same line (actually, when the line fills up it will wrap around, but ignore that.). In order to do this, your print statement should have end=" " in it. For example, print(name,end=" ")  will keep the next print statement from starting a new line. Be sure there is a space between these quotes or your numbers will run together. Use a single space as that is what the grading program expects. Use a 'for' loop and a range() function. 
  >>>problem1_6()
  1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97 99
"""
#%%
def problem1_6():
  for x in range(1,101, 2):
    print(x,end=' ')

#%% 
"""
Problem 1_7:
Write a function problem1_7() that computes the area of a trapezoid. Here is the formula: A = (1/2)(b1+b2)h. In the formula b1 is the length of one of the bases, b2 the other. The height is h and the area is A. Basically, this takes the average of the two bases times the height. For a rectangle b1 = b2, so this reduces to b1*h. This means that you can do a pretty good test of the correctness of your function using a rectangle (that way you can compute the answer in your head). Use input statements to ask for the bases and the height. Convert these input strings to real numbers using float(). Print the output nicely exactly like mine below.

Tip: Be careful that your output on the test case below is exactly as shown so that the auto-grader judges your output correctly.  See the other test run below.

In[105]: 

problem1_7()

Enter the length of one of the bases: 3

Enter the length of the other base: 4

Enter the height: 8
The area of a trapezoid with bases 3.0 and 4.0 and height 8.0 is 28.0

"""  
#%%
def problem1_7():
    b1 = float(input('Enter the length of one of the bases:'))
    b2 = float(input('Enter the length of the other base:'))
    h = float(input('Enter the height:'))
    area = ((b1+b2) / 2) * h
    if b1 == b2:
      print('The area of a trapezoid with bases', b1, 'and', b2, 'and height', h, 'is', b1*h)
    else:
      print('The area of a trapezoid with bases', b1, 'and', b2, 'and height', h, 'is', area)

#%%
"""
Test run. In grading, expect different input numbers to be used.

problem1_7()

Enter the length of one of the bases: 10

Enter the length of the other base: 11

Enter the height: 12
The area of a trapezoid with bases 10.0 and 11.0 and height 12.0 is 126.0

"""
