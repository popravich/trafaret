import sys
import doctest
import trafaret
from trafaret import utils, extras, visitor


if __name__ == '__main__':
    errors = 0
    for mod in (trafaret,
                extras,
                utils,
                visitor,
                ):
        errors += doctest.testmod(m=mod).failed
    sys.exit(int(errors > 0))
