from array import array
from multiprocessing.dummy import Array

def double_zero(array_input_rez):
    i=0
    while i<len(array_input_rez):
        if array_input_rez[i]==0:
            array_input_rez.insert(i+1,0)
            i+=2
        else:i+=1
    return(array_input_rez)
str_inp=input("Введи текст не менше п'яти символів ")
try:
    array_input=list(map(int,str_inp))
    if len(array_input)<len(double_zero(array_input)):
        print('Zeros doubled',double_zero(array_input))
    else:print('Does not contain zeros',double_zero(array_input))
except ValueError:print('Type only numbers')

