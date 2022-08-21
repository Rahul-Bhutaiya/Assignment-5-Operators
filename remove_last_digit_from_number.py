"""
Write a python script to remove the last digit from a given number. (for example, if
user enters 2534 then your output should be 253)
"""
number=int(input('Enter a Number : '))
number//=10
print('After Removing Last Digit From Entered Number :',number)