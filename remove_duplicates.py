
def remove_duplicates(array):
    array_edit=array.copy()
    i=0
    while i<(len(array_edit)-1):
        if array_edit[i]==array_edit[i+1]:
            array_edit.pop(i+1)
        else:i+=1
    return(array_edit)
str_inp=input("Enter number ")
try:
    array_input=list(map(int,str_inp))
    array_input_rez=remove_duplicates(array_input)
    if len(array_input)!=len(array_input_rez):
        print('Duplicates remove',array_input_rez)
    else:
        print('Does not contain duplicates',array_input)
except ValueError:print('Type only numbers')