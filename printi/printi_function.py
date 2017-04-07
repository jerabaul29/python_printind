from __future__ import print_function
import traceback
from printi import printi_package_depth


def printi_function_call(string_in, indent_level=None, indent_pattern='  ', debug=0):
    assert type(string_in) == str

    if indent_level is None:
        extracted_stack = traceback.extract_stack()
        depth_in = len(extracted_stack) - printi_package_depth

        if debug:
            print("depth_in: " + str(depth_in))
            traceback.print_stack()

        prefix = depth_in * indent_pattern

        print(prefix + string_in)

    else:
        assert type(indent_level) == int
        prefix = indent_level * indent_pattern

        print(prefix + string_in)
