import time
import inspect


def log(fn):
    """
    Add your code here or call it from here   
    """
    def wrapper(*args, **kwargs):
        # Caluclate execution time 
        start_time = time.time()
        result = fn(*args, **kwargs)
        exe_time = round(time.time() - start_time, 2)

        # Get function parameters
        sig = inspect.signature(fn)
        bound = sig.bind(*args, **kwargs)
        bound.apply_defaults()
        full_args = bound.arguments
        
        # Variables to store args and kwargs strings
        s_args = ""
        s_kwargs = ""
        
        # s_args, s_kwargs creation 
        for i, (name, value) in enumerate(full_args.items()):
            if i < len(args):
                s_args += f"{name}={value}, "
            else:
                s_kwargs += f"{name}={value}, "

        # Strip last comma i each string
        s_args = s_args.rstrip(", ")
        s_kwargs = s_kwargs.rstrip(", ")

        # Finally write log entry (for example: foo; args: a=1, b=2; kwargs: c=3; execution time: 0.12 sec.) to log file
        with open("log.txt", "a") as f:
            content = f"{fn.__name__}; args: {s_args}; kwargs: {s_kwargs}; execution time: {exe_time} sec.\n"
            f.write(content)
        
        return result 
    return wrapper

