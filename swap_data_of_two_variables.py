#Write a python script to swap data of two variables

var_1=eval(input('Enter Value of First Variable : '))
var_2=eval(input('Enter Value of Second Variable : '))
print('Variable_1 =',var_1,'\nVariable_2 =',var_2)
var_1,var_2=var_2,var_1
print('After Swapping Value of Both Variables...')
print('Variable_1 =',var_1,'Variable_2 =',var_2)