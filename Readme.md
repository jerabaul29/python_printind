# Printind

## Aim

**printind** uses the python *traceback* package to indent the print function. This is especially nice when, for example, debugging, as this helps giving an overview of how functions call each other.

In addition to printing functions, decorators for tracking function calls are provided.

## Use and example

Use it like (as a print function):

```
from printind.printind_function import printi, printiv

printi('my string')

a = 4
printiv(a)
```

Use it like (as a decorator):

```
from printind.printind_decorators import printi_function_call_wrapper as printidf
from printind.printind_decorators import printi_all_method_calls as printidc

@printidf
  def some_function():
      printi("this is the core")

  some_function()


@printidc()
class some_class_2(object):
    def __init__(self):
        printi("this is the init core")

    def some_method(self):
        printi("this is a method")

some_instance = some_class_2()
some_instance.some_method()
```

For an illustrative code example see the **tests** folder. This can also be used for testing in development: ```pytest -v -s .``` from the root of the module.

## Installation

pip install printind

## Keywords

print, print function, indent, automatic indent, stack, depth function call, debugging.

# Technical note

## Packaging

The module is packaged by:

```
python setup.py sdist
twine upload dist/printind-3.0.tar.gz
```

*NOTE* that twine is using the credentials stored in .pypirc
