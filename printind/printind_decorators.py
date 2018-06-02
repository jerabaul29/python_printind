from printind.printind_function import printi
import functools


def printi_function_call_wrapper(wrapped, class_containing=None):
    """Decorator to printi function calls."""
    @functools.wraps(wrapped)
    def _wrapper(*args, **kwargs):
        if class_containing is None:
            printi("call {} --".format(wrapped.__name__))
            result = wrapped(*args, **kwargs)
            printi("exit {} --".format(wrapped.__name__))
            return(result)
        else:
            printi("call {} from {} --".format(wrapped.__name__, class_containing))
            result = wrapped(*args, **kwargs)
            printi("exit {} from {} --".format(wrapped.__name__, class_containing))
            return(result)
    return _wrapper


def decorator_on_all_methods(decorator):
    """Apply a decorator on all method calls."""
    def decorate(cls):
        for attr in cls.__dict__:
            if callable(getattr(cls, attr)):
                setattr(cls, attr, decorator(getattr(cls, attr), cls.__name__))
        return cls
    return decorate


def printi_all_method_calls():
    """Class decorator to printi all method calls."""
    return(decorator_on_all_methods(printi_function_call_wrapper))
