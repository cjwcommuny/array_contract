import inspect


class Trigger:
    dtype_check_trigger: bool = __debug__
    ndim_check_trigger: bool = __debug__
    shape_check_trigger: bool = __debug__


class __Closure:
    def __init__(self, func, constraints, kwconstraints):
        self.func = func
        self.func_signature: inspect.Signature = inspect.signature(func)
        self.bound_constraints = self.func_signature.bind_partial(*constraints, **kwconstraints).arguments

    def __call__(self, *args, **kwargs):
        raise NotImplementedError()


class _MethodDecoratorAdaptor(object):
    def __init__(self, decorator, func):
        self.decorator = decorator
        self.func = func
    def __call__(self, *args, **kwargs):
        return self.decorator(self.func)(*args, **kwargs)
    def __get__(self, instance, owner):
        return self.decorator(self.func.__get__(instance, owner))


def auto_adapt_to_methods(decorator):
    """Allows you to use the same decorator on methods and functions,
    hiding the self argument from the decorator."""
    def adapt(func):
        return _MethodDecoratorAdaptor(decorator, func)
    return adapt