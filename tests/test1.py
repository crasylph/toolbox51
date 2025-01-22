
from typing import Callable
import functools
import traceback

from toolbox51 import logger


def wrapper_factory_default(func: Callable, message: str = ""):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"{message} start", stacklevel = 2)
        result = func(*args, **kwargs)
        logger.info(f"{message} end", stacklevel = 2)
        return result
    return wrapper

def wrapper_factory_with_exceptions(func: Callable, message: str = ""):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"{message} start", stacklevel = 2)
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            logger.warning(f"{message} failed with exception: {e}")
            traceback.print_exc()
            result = None #TODO: 是否需要根据参数数量返回默认值？
        logger.info(f"{message} end", stacklevel = 2)
        return result
    return wrapper

def decorator(
    *args, 
    message = None, with_exceptions = None
):
    if(len(args) == 1 and callable(args[0])):
        func = args[0]
        wrapper = wrapper_factory_default(func)
        return wrapper
    else:
        func = None
    def f(func):
        wrapper = wrapper_factory_default(func)
        return wrapper
    return f


if(__name__ == "__main__"):

    @decorator
    def func1(a, b):
        return a + b

    print(func1(2, 3))



    @decorator(10)
    def func2(a, b):
        return a + b

    print(func2(2, 3))