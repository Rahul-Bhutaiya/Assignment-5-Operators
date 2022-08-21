#Write a python script to use IS operator to display if both variables are the same object or not?

var_1=eval(input('Enter First Value : '))
var_2=eval(input('Enter Second Value : '))

print('Both Variable are The Same Object')if var_1 is var_2 else print('Both Variable are not The Same Object')