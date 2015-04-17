"""Define a function max_of_three() that takes three 
numbers as arguments and returns the largest of them."""

# Solution by Nick Rameau - @R4meau
def max_of_three(num1, num2, num3):
  if num1 > num2 > num3:
    return num1
  elif num1 < num2 < num3:
    return num3
  else: return num2

# Solution by Your Name - @YourUsername
# You can add your solution here.
# A good way to show other people your solution
# to this exercise. Remember to comment it out.
# I'll be waiting for your pull request.
# And please, leave this comment block intact so other people
# Can see it later too.

#test
print max_of_three(2, 3, 4)
print max_of_three(4, 3, 2)
print max_of_three(2, 4, 3)