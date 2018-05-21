from __future__ import print_function
import traceback
from printind import initial_depth
import inspect


def printi(string_in, indent_level=None, indent_pattern='  ', debug=0):
    """Print with stack depth indentation for easy visual debugging."""
    assert type(string_in) == str

    if indent_level is None:
        extracted_stack = traceback.extract_stack()
        depth_in = len(extracted_stack) - initial_depth

        if debug:
            print("depth_in: " + str(depth_in))
            traceback.print_stack()

        prefix = depth_in * indent_pattern

        print(prefix + string_in)

    else:
        assert type(indent_level) == int
        prefix = indent_level * indent_pattern

        print(prefix + string_in)


def printiv(variable, indent_level=None, indent_pattern='  ', debug=0, remove_self=True):
    """Print a variable and its content with stack depth indentation. Built based
    on some code released at:

    https://stackoverflow.com/questions/2749796/how-to-get-the-original-variable-name-of-variable-passed-to-a-function"""

    frame = inspect.currentframe()
    frame = inspect.getouterframes(frame)[1]
    string = inspect.getframeinfo(frame[0]).code_context[0].strip()
    args = string[string.find('(') + 1:-1].split(',')

    names = []
    for i in args:
        if i.find('=') != -1:
            names.append(i.split('=')[1].strip())

        else:
            names.append(i)

    crrt_name = names[0]
    if remove_self:
        if crrt_name[0:5] == "self.":
            crrt_name = crrt_name[5:]

    printi("{} = {}".format(crrt_name, variable))
