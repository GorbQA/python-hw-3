from array import array
from multiprocessing.dummy import Array

def double_zero(array):
    array_edit=array.copy()
    i=0
    while i<len(array_edit):
        if array_edit[i]==0:
            array_edit.insert(i+1,0)
            i+=2
        else:i+=1
    return (array_edit)
str_inp="10230450"
try:
    array_input=list(map(int,str_inp))
    array_input_rez=double_zero(array_input)
    if len(array_input)!=len(array_input_rez):
        print('Zeros doubled',array_input_rez)
    else:
        print('Does not contain zeros',array_input)
except ValueError:print('Type only numbers')

