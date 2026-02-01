import time

def time_function(func, *args, **kwargs):
    start = time.time()
    out = func(*args, **kwargs)
    return out, (time.time() - start) * 1000
