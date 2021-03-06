'''
Merge strategies for the deep_merge function
'''

from pydeepmerge.strategies._strategies import (  # noqa: F401
    meta_operator_merge,
)

# The merge strategy prefer_right is still a part of this package's
# namespace, but is added dynamically at the top level package's init file
# to avoid some errors with circular imports
