from ntpath import join
import string
import sys
def calc(left_operand, right_operand, operation):
    l_int, r_int, op = left_operand, right_operand, operation
    match op:
        case '*':
            rez=l_int*r_int
        case '+':
            rez=l_int+r_int
        case '-':
            rez=l_int-r_int
        case '/':
            rez=l_int/r_int
        case '%':
            rez=l_int%r_int
    print(l_int,op,r_int,"=",int(rez))
list_sys=sys.argv[1:]
str_list_sys="".join(list_sys)
for i in range(len(str_list_sys)):
    op=str_list_sys[i]
    if op in '+-/*%':
        operator=op
try:
    spl_str_list_sys=str_list_sys.split(operator)
    if len(spl_str_list_sys)>2:
        print("Only one operator allowed")
    left_op = int(spl_str_list_sys[0])
    righ_op = int(spl_str_list_sys[1])
    calc(left_op,righ_op,operator)
except ValueError:print('Left and Right operands must be int')
except ZeroDivisionError: print("Division by zero is not allowed")
except NameError:print("Arithmetic operator is not defined")