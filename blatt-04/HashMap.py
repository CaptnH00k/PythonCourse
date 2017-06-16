#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright 2017, University of Freiburg,
Chair of Algorithms and Data Structures.
Author: Leon Gnädinger <leon.gnaedinger@gmail.com>.
"""


class HashMap:
    """
    HashMap Algorithm implemented in Python
    """
    def __init__(self, size):
        """
        On init you have to set the size of your HashMap.
        Choose this cautious, because this limits the count
        of elements the HashMap can hold.

        Args:
            size (int): Size of the HashMap

        Examples:
            >>> hm = HashMap(42)
            >>> len(hm.field)
            42
            >>> hm.size
            42
        """
        self.size = size
        # generates a list with the size size. Default values are None.
        self.field = [None] * self.size

    def _hash(self, key_as_int):
        """
        Internal function to generate the hash for the integer representation
        of key. This hash function simply calculates key_as_int modulo
        self.size.

        Args:
            key_as_int (int): integer representation of key

        Returns:
            hash value as integer

        Examples:
            >>> hm = HashMap(5)
            >>> hm._hash(10)
            0
            >>> hm._hash(3)
            3
            >>> hm._hash(17)
            2
            >>> hm2 = HashMap(7)
            >>> hm2._hash(17)
            3
        """
        return key_as_int % self.size

    def _string_key_to_int(self, key):
        """
        This internal functions calculates an integer value of key
        We do this by adding all ascii values of the different characters
        key insists of together.

        Note:
            different keys can have the same int value!

        Args:
            key (string): A string only insisting of ascii characters

        Returns:
            integer value representing key

        Examples:
            >>> hm = HashMap(5)
            >>> hm._string_key_to_int('doof')
            424
        """
        int_representing_key = 0
        for c in key:
            int_representing_key += ord(c)
        return int_representing_key

    def insert(self, key, value):
        """
        This method adds a key value pair into the HashMap Datastracture.
        If key is already in Datastracture, it will be overwritten.

        Args:
            key (string): A string only insisting of ascii characters
            int (int)   : A integer value saved to key

        Examples:
            >>> hm = HashMap(4)
            >>> hm.insert('test', 13)
            >>> ('test', 13) in hm.field
            True
            >>> hm.insert('test', 14)
            >>> ('test', 13) in hm.field
            False
            >>> ('test', 14) in hm.field
            True
            >>> hm.insert('test2', 42)
            >>> hm.insert('test3', 43)
            >>> hm.insert('test4', 44)
            >>> hm.insert('test5', 45)
            Traceback (most recent call last):
              ...
            Exception: Couldn't insert key, HashMap full
        """
        # calculate hash for key. We have to convert string to an int and than
        # hash it.
        hashed_key = self._hash(self._string_key_to_int(key))
        # in the worst case we have to go through all fields, never more!
        for i in range(0, self.size):
            # make sure we don't overflow the field size with modulo magic
            mod_index = (hashed_key + i) % self.size
            # if field is empty (none) or key equals our insert key,
            # set it to our key/value pair
            if(self.field[mod_index] is None or
               self.field[mod_index][0] == key):
                self.field[mod_index] = (key, value)
                return
        # seems like we didn't find a matching place for this key/value
        # pair. Throw an exception.
        raise Exception("Couldn't insert key, HashMap full")

    def lookup(self, key):
        """
        Returns value paired with key if key was found in HashMap. Otherwise
        False.
        Args:
            key (string): A string only insisting of ascii characters

        Returns:
            (int) value if key was found, otherwise False

        Examples:
            >>> hm = HashMap(5)
            >>> hm.insert('test1', 42)
            >>> hm.insert('test3', 44)
            >>> hm.lookup('test1')
            42
            >>> hm.lookup('test3')
            44
            >>> hm.lookup('test2')
            False
        """
        # calculate hash for key. We have to convert string to an int and than
        # hash it.
        hashed_key = self._hash(self._string_key_to_int(key))
        # in the worst case we have to go through all fields, never more!
        for i in range(0, self.size):
            # make sure we don't overflow the field size with modulo magic
            mod_index = (hashed_key + i) % self.size
            # if we found a None field, we didn't insert a matching key yet.
            if(self.field[mod_index] is None):
                break
            elif(self.field[mod_index][0] == key):
                # found a matching key, return value
                return self.field[mod_index][1]
        return False

    def get_key_value_pairs(self):
        """
        Returns all key/value pairs in HashMap as list

        Returns:
            List of all (key, value) pairs

        Examples:
            >>> hm = HashMap(4)
            >>> hm.insert('test', 42)
            >>> hm.insert('tset', 43)
            >>> hm.insert('test2', 44)
            >>> kv = hm.get_key_value_pairs()
            >>> ('test', 42) in kv
            True
            >>> ('tset', 43) in kv
            True
            >>> ('test2', 44) in kv
            True
            >>> len(kv)
            3
        """
        key_value_pairs = []
        for key_value in self.field:
            if key_value is not None:
                key_value_pairs.append(key_value)
        return key_value_pairs


if __name__ == "__main__":
    hm = HashMap(5)
    hm.insert('test', 5)
    hm.insert('test2', 7)
    print(hm.lookup('test'))
    print(hm.lookup('test2'))
    hm.insert('doof', 3)
    print(hm.lookup('doof'))
    print(hm.lookup('xyz'))
