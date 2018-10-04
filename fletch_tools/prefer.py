"""Deal with saved configs."""

import shelve
import os
from os import path as p
from .good_input import get_input

class Prefs:
    """A class to interface with a preference shelve."""
    # Find users home dir for defaults:
    home = p.expanduser('~')

    def __init__(self, location=home, foldername='.fletch_prefs'):
        location = p.join(location, foldername)
        if not p.exists(location):
            os.makedirs(location)

        self.file = p.join(location, 'settings')

    def get(self, key):
        prefs = shelve.open(self.file)
        try:
            value = prefs[key]
        except:
            value = None

        prefs.close()
        return value

    def smart_get(
            self,
            key,
            input_func=get_input,
            expected_type='str',
            message = "'{}' not specified, please define:"
            ):
        """A function to be run in case the requested key does not
        exist can be specified.
        """
        prefs = shelve.open(self.file)
        try:
            value = prefs[key]
        except:
            prefs[key] = input_func(message.format(key),
                expected_type)
            value = prefs[key]

        prefs.close()
        return value

    def set(self, key, value):
        prefs = shelve.open(self.file)
        prefs[key] = value
        prefs.close()

if __name__ == '__main__':

    test_prefs = Prefs(foldername='.test_prefs')
    print(test_prefs.smart_get('name'))
    print(test_prefs.get('name'))
    test_prefs.set('name', 'Fletcher Graham')
    print(test_prefs.get('name'))
