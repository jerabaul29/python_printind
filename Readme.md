# Printind

## Aim

**printind** uses the python *traceback* package to indent the print function. This is especially nice when, for example, debugging, as this helps giving an overview of how functions call each other.

## Use and example

Use it like:

```
from printind.printind_function import printi

printi('my string')
```

For an illustrative code example see the **example** folder. The output of *example.py* called in terminal, or through iPython should look like:

```
this is the script
the script is executing
  start f_1
  f_1 again!
    start f_2
      start f_3
    f_2, this is the end!
    start f_3
  end f_1
end of the script

```

## Installation

pip install printind

## Keywords

print, print function, indent, automatic indent, stack, depth function call, debugging.
