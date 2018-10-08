# Do a series of things with a given path. Typically used for importing data
# that's not saved in the same place as our program, letting you not have to
# change wdir back when you want to store, say, a graph.
# You use it as >>>wdir([path_you_want_to_work_in])
# to set a path for your current project or otherwise
# >>>with wdir([path]) [do_something]

from contextlib import contextmanager
import os

@contextmanager
def wdir(path):
    current_dir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(current_dir)
