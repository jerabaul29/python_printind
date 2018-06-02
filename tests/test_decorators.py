from printind.printind_decorators import printi_function_call_wrapper as printidf
from printind.printind_decorators import printi_all_method_calls as printidc
from printind.printind_decorators import decorator_on_all_methods as printi_methods
from printind.printind_function import printi
from callifile.callifile_functions import callifile


def test_printi_function_call_wrapper():
    printi("enter test_printi_function_call_wrapper")

    @printidf
    def some_function():
        printi("this is the core")

    some_function()


def test_decorator_on_all_methods():
    @printi_methods(printidf)
    class some_class(object):
        def __init__(self):
            printi("this is the init core")

        def some_method(self):
            printi("this is a method")

    some_instance = some_class()
    some_instance.some_method()


def test_printi_all_method_calls():
    @printidc()
    class some_class_2(object):
        def __init__(self):
            printi("this is the init core")

        def some_method(self):
            printi("this is a method")

    some_instance = some_class_2()
    some_instance.some_method()


if __name__ == "__main__":
    printi("Main call")

    callifile(verbose=False)