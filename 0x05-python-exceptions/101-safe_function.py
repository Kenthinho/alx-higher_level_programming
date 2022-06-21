#!/usr/bin/python3
def safe_functional(fct, *args):
    import sys
    try:
        var = fct(*args)
        return var
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
