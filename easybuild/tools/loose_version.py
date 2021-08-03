# This file contains the LooseVersion class based on the class with the same name
# as present in Python 3.7.4 distutils.
# The original class is licensed under the Python Software Foundation License Version 2.
# It was slightly simplified as needed to make it shorter and easier to read.
# In particular the following changes were made:
# - Subclass object directly instead of abstract Version class
# - Fully init the class in the constructor removing the parse method
# - Always set self.vstring and self.version
# - Shorten the comparison operators as the NotImplemented case doesn't apply anymore
# - Changes to documentation and formatting

import re


class LooseVersion(object):
    """Version numbering for anarchists and software realists.

    A version number consists of a series of numbers,
    separated by either periods or strings of letters.
    When comparing version numbers, the numeric components will be compared
    numerically, and the alphabetic components lexically.
    """

    component_re = re.compile(r'(\d+ | [a-z]+ | \.)', re.VERBOSE)

    def __init__(self, vstring=None):
        self.vstring = vstring
        if vstring:
            components = [x for x in self.component_re.split(vstring)
                          if x and x != '.']
            for i, obj in enumerate(components):
                try:
                    components[i] = int(obj)
                except ValueError:
                    pass
            self.version = components
        else:
            self.version = None

    def __str__(self):
        return self.vstring

    def __repr__(self):
        return "LooseVersion ('%s')" % str(self)

    def _cmp(self, other):
        """Rich comparison method used by the operators below"""
        if isinstance(other, str):
            other = LooseVersion(other)

        if self.version == other.version:
            return 0
        if self.version < other.version:
            return -1
        if self.version > other.version:
            return 1

    def __eq__(self, other):
        return self._cmp(other) == 0

    def __lt__(self, other):
        return self._cmp(other) < 0

    def __le__(self, other):
        return self._cmp(other) <= 0

    def __gt__(self, other):
        return self._cmp(other) > 0

    def __ge__(self, other):
        return self._cmp(other) >= 0
