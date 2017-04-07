from printi.printi_function import printi_function_call


def f_1(debug=0):
    printi_function_call('start f_1', debug=debug)
    printi_function_call('f_1 again!')

    f_2()

    f_3()

    printi_function_call('end f_1')


def f_2():
    printi_function_call('start f_2')

    f_3()

    printi_function_call('f_2, this is the end!')


def f_3():
    printi_function_call('start f_3')

printi_function_call('this is the script')
printi_function_call('the script is executing')
f_1()
printi_function_call('end of the script')
