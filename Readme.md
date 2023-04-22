Arithmetic Formatter
# Functions used in Aritmentic formatter
The arithmetic_arranger() function uses the following functions:

1.  split(): This function is a built-in method in Python that splits a string into a list of substrings based on a specified delimiter. In this code, it is used to split the input problems into individual pieces, which include the first operand, operator, and second operand.
  Example:
  problems = ["10 + 11","109 + 999"]
      for x in problems:
        pieces = x.split()
        print(pieces)
# output
  ['10', '+', '11']
  ['109', '+', '999']
  
  
2.  isdigit(): This function is a built-in method in Python that checks if a string contains only digits (0-9). It is used in this code to validate that the operands in first_operand and second_operand contain only digits.
    x = 100
    print(str(x).isdigit())
    print(str(x).isnumeric())
    #output
    True 
    True
3.  max(): This function is a built-in function in Python that returns the maximum value among a sequence of numbers. In this code, it is used to determine the maximum length of the first and second operands in order to align the output properly.

4.  str(): This function is a built-in function in Python that converts a value to a string. It is used in this code to convert integer values to strings in order to concatenate them with other strings.

5.  int(): This function is a built-in function in Python that converts a value to an integer. It is used in this code to convert the string representation of operands to integer values in order to perform arithmetic operations and obtain the answers if answer parameter is set to True.

6.  String methods: The code uses various string methods such as ljust(), rjust(), and join() to align the operands and operators properly and create the final formatted string arranged_problems with appropriate spaces and line breaks.
