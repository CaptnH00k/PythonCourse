"""
Copyright 2017, University of Freiburg,
Chair of Algorithms and Data Structures.
Author: Hannah Bast <bast@cs.uni-freiburg.de>,
        Axel Lehmann <lehmann@cs.uni-freiburg.de>.
"""


class LinkedList:
    """ A doubly linked list.

    >>> LinkedListItem.num_items = 0
    >>> item_C = LinkedListItem(1, 'C')
    >>> item_A = LinkedListItem(2, 'A')
    >>> item_B = LinkedListItem(3, 'B')
    >>> item_D = LinkedListItem(4, 'D')
    >>> ll = LinkedList()
    >>> ll.insert_before(item_C, None)
    >>> ll.insert_before(item_A, item_C)
    >>> ll.insert_before(item_B, item_C)
    >>> ll.insert_before(item_D, None)
    >>> ll
    first = #2, last = #4
    [id = #2, prev = #0, next = #3, key = 2, val = A]
    [id = #3, prev = #2, next = #1, key = 3, val = B]
    [id = #1, prev = #3, next = #4, key = 1, val = C]
    [id = #4, prev = #1, next = #0, key = 4, val = D]

    """

    def __init__(self):
        """ Create an initially empty linked list. """

        self.first = None
        self.last = None
        self._count = 0

    def __repr__(self):
        """" Linked list as humand-readable string. """

        result = \
            "first = #" + str(0 if self.first is None else self.first.id) \
            + ", last = #" + str(0 if self.last is None else self.last.id)
        item = self.first
        while item is not None:
            result += "\n" + str(item)
            item = item.next
        return result

    def empty(self):
        return self._count < 1

    def insert_before(self, new_item, next_item):
        """ Insert new_item before next_item. If next_item is None, insert at
        end. """

        # New prev pointers.
        if next_item is None:
            new_item.prev = self.last
            self.last = new_item
        else:
            new_item.prev = next_item.prev
            next_item.prev = new_item
        # New next pointers.
        if new_item.prev is None:
            new_item.next = self.first
            self.first = new_item
        else:
            new_item.next = next_item
            new_item.prev.next = new_item
        self._count += 1

    def remove(self, item):
        """ Remove a given item from the list.

        >>> LinkedListItem.num_items = 0
        >>> item_C = LinkedListItem(1, 'C')
        >>> item_A = LinkedListItem(2, 'A')
        >>> item_B = LinkedListItem(3, 'B')
        >>> item_D = LinkedListItem(4, 'D')
        >>> ll = LinkedList()
        >>> ll.insert_before(item_C, None)
        >>> ll.insert_before(item_A, item_C)
        >>> ll.insert_before(item_B, item_C)
        >>> ll.insert_before(item_D, None)
        >>> ll
        first = #2, last = #4
        [id = #2, prev = #0, next = #3, key = 2, val = A]
        [id = #3, prev = #2, next = #1, key = 3, val = B]
        [id = #1, prev = #3, next = #4, key = 1, val = C]
        [id = #4, prev = #1, next = #0, key = 4, val = D]
        >>> ll.remove(item_D) == item_D
        True
        >>> ll
        first = #2, last = #1
        [id = #2, prev = #0, next = #3, key = 2, val = A]
        [id = #3, prev = #2, next = #1, key = 3, val = B]
        [id = #1, prev = #3, next = #0, key = 1, val = C]
        >>> ll.remove(item_B) == item_B
        True
        >>> ll
        first = #2, last = #1
        [id = #2, prev = #0, next = #1, key = 2, val = A]
        [id = #1, prev = #2, next = #0, key = 1, val = C]
        >>> ll.remove(item_A) == item_A
        True
        >>> ll
        first = #1, last = #1
        [id = #1, prev = #0, next = #0, key = 1, val = C]
        >>> ll.remove(item_C) == item_C
        True
        >>> ll
        first = #0, last = #0
        """
        if item.prev is None:
            self.first = item.next
        else:
            item.prev.next = item.next
        if item.next is None:
            self.last = item.prev
        else:
            item.next.prev = item.prev
        item.next = None
        item.prev = None
        self._count -= 1
        return item

    def reverse(self):
        """ Reverse the order of elements in O(n).

        >>> LinkedListItem.num_items = 0
        >>> item_C = LinkedListItem(1, 'C')
        >>> item_A = LinkedListItem(2, 'A')
        >>> item_B = LinkedListItem(3, 'B')
        >>> item_D = LinkedListItem(4, 'D')

        >>> ll = LinkedList()
        >>> ll
        first = #0, last = #0
        >>> ll.reverse()
        >>> ll
        first = #0, last = #0

        >>> ll.insert_before(item_C, None)
        >>> ll
        first = #1, last = #1
        [id = #1, prev = #0, next = #0, key = 1, val = C]
        >>> ll.reverse()
        >>> ll
        first = #1, last = #1
        [id = #1, prev = #0, next = #0, key = 1, val = C]


        >>> ll.insert_before(item_A, item_C)
        >>> ll.insert_before(item_B, item_C)
        >>> ll.insert_before(item_D, None)
        >>> ll
        first = #2, last = #4
        [id = #2, prev = #0, next = #3, key = 2, val = A]
        [id = #3, prev = #2, next = #1, key = 3, val = B]
        [id = #1, prev = #3, next = #4, key = 1, val = C]
        [id = #4, prev = #1, next = #0, key = 4, val = D]
        >>> ll.reverse()
        >>> ll
        first = #4, last = #2
        [id = #4, prev = #0, next = #1, key = 4, val = D]
        [id = #1, prev = #4, next = #3, key = 1, val = C]
        [id = #3, prev = #1, next = #2, key = 3, val = B]
        [id = #2, prev = #3, next = #0, key = 2, val = A]
        """
        current = self.first
        while current is not None:
            current.prev, current.next = current.next, current.prev
            current = current.prev
        self.first, self.last = self.last, self.first

    def splice(self, l1, l2):
        """
        Cut out the segment given by head and tail. Return it as a new list.

        >>> LinkedListItem.num_items = 0
        >>> item_C = LinkedListItem(1, 'C')
        >>> item_A = LinkedListItem(2, 'A')
        >>> item_B = LinkedListItem(3, 'B')
        >>> item_D = LinkedListItem(4, 'D')
        >>> ll = LinkedList()
        >>> ll.insert_before(item_C, None)
        >>> ll.insert_before(item_A, item_C)
        >>> ll.insert_before(item_B, item_C)
        >>> ll.insert_before(item_D, None)
        >>> ll
        first = #2, last = #4
        [id = #2, prev = #0, next = #3, key = 2, val = A]
        [id = #3, prev = #2, next = #1, key = 3, val = B]
        [id = #1, prev = #3, next = #4, key = 1, val = C]
        [id = #4, prev = #1, next = #0, key = 4, val = D]

        >>> sl1 = ll.splice(item_B, item_C)
        >>> ll
        first = #2, last = #4
        [id = #2, prev = #0, next = #4, key = 2, val = A]
        [id = #4, prev = #2, next = #0, key = 4, val = D]
        >>> sl1
        first = #3, last = #1
        [id = #3, prev = #0, next = #1, key = 3, val = B]
        [id = #1, prev = #3, next = #0, key = 1, val = C]

        >>> sl2 = sl1.splice(item_B, item_C)
        >>> ll
        first = #2, last = #4
        [id = #2, prev = #0, next = #4, key = 2, val = A]
        [id = #4, prev = #2, next = #0, key = 4, val = D]
        >>> sl1
        first = #0, last = #0
        >>> sl2
        first = #3, last = #1
        [id = #3, prev = #0, next = #1, key = 3, val = B]
        [id = #1, prev = #3, next = #0, key = 1, val = C]
        """
        # Cut from old list.
        if l1.prev is None:
            self.first = l2.next
        else:
            l1.prev.next = l2.next
        if l2.next is None:
            self.last = l1.prev
        else:
            l2.next.prev = l1.prev

        # Generate new list
        new_list = LinkedList()
        new_list.first = l1
        new_list.last = l2
        l1.prev = None
        l2.next = None
        return new_list


class LinkedListItem:
    """
    An item from a doubly linked list.

    """

    num_items = 0

    def __init__(self, key, value):
        """ Create an item with given value.

        >>> LinkedListItem.num_items = 0
        >>> LinkedListItem(1, 'A')
        [id = #1, prev = #0, next = #0, key = 1, val = A]
        >>> LinkedListItem(2, 'B')
        [id = #2, prev = #0, next = #0, key = 2, val = B]
        """
        LinkedListItem.num_items += 1
        self.id = LinkedListItem.num_items
        self.next = None
        self.prev = None
        self.key = key
        self.value = value

    def __repr__(self):
        """ Item as human-readable string.

        """
        return "[id = #" + str(self.id) \
            + ", prev = #" + str(0 if self.prev is None else self.prev.id) \
            + ", next = #" + str(0 if self.next is None else self.next.id) \
            + ", key = " + str(self.key) \
            + ", val = " + str(self.value) + "]"
