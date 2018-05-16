from printind.printind_function import printi, printiv


def test_printi_functions():
    def f_1(debug=0):
        printi('start f_1', debug=debug)
        printi('f_1 again!')

        f_2()

        f_3()

        printi('end f_1')

    def f_2():
        printi('start f_2')

        f_3()

        printi('f_2, this is the end!')

    def f_3():
        printi('start f_3')

        a = 4
        printiv(a)

    printi('this is the script')
    printi('the script is executing')
    f_1()
    printi('end of the script')
