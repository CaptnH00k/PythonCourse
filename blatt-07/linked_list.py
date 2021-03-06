"""
Copyright 2017, University of Freiburg,
Chair of Algorithms and Data Structures.
Author: Hannah Bast <bast@cs.uni-freiburg.de>
"""


class LinkedList:
    """
    A doubly-linked list of items of type LinkedListItem.

    >>> LinkedListItem.num_items = 0
    >>> ll = LinkedList()
    >>> item_C = LinkedListItem('C')
    >>> item_A = LinkedListItem('A')
    >>> item_B = LinkedListItem('B')
    >>> item_D = LinkedListItem('D')
    >>> ll.insert_before(item_C, None)    # Insert item C into the empty list.
    >>> ll.insert_before(item_A, item_C)  # Insert item A before item C.
    >>> ll.insert_before(item_B, item_C)  # Insert item B between items A and C
    >>> ll.insert_before(item_D, None)    # Insert item D at the end.
    >>> ll
    first = #2, last = #4
    [id = #2, prev = #0, next = #3, val = A]
    [id = #3, prev = #2, next = #1, val = B]
    [id = #1, prev = #3, next = #4, val = C]
    [id = #4, prev = #1, next = #0, val = D]
    """

    def __init__(self):
        """ Construct an empty linked list. """

        self.first = None
        self.last = None

    def __repr__(self):
        """ The current state of the list in human-readable form. """

        result = \
            "first = #" + str(0 if self.first is None else self.first.id) \
            + ", last = #" + str(0 if self.last is None else self.last.id)
        item = self.first
        while item is not None:
            result += "\n" + str(item)
            item = item.next
        return result

    def insert_before(self, new_item, next_item):
        """ Insert new_item before next_item. If next_item is None, insert
        new_item at the end of the list. """

        # First set the (two) new prev pointers (including possibly last).
        if next_item is not None:
            new_item.prev = next_item.prev
            next_item.prev = new_item
        else:
            new_item.prev = self.last
            self.last = new_item
        # Then set the (two) new next pointers (including possibly first).
        if new_item.prev is not None:
            new_item.next = next_item
            new_item.prev.next = new_item
        else:
            new_item.next = self.first
            self.first = new_item

    def reverse(self):
        """
        Reverse this LinkedList so that first element is last, second element
        is the element before last... last element is first.

        >>> LinkedListItem.num_items = 0
        >>> ll = LinkedList()
        >>> item_C = LinkedListItem('C')
        >>> item_A = LinkedListItem('A')
        >>> item_B = LinkedListItem('B')
        >>> item_D = LinkedListItem('D')
        >>> ll.insert_before(item_C, None)
        >>> ll.insert_before(item_A, item_C)
        >>> ll.insert_before(item_B, item_C)
        >>> ll.insert_before(item_D, None)
        >>> ll
        first = #2, last = #4
        [id = #2, prev = #0, next = #3, val = A]
        [id = #3, prev = #2, next = #1, val = B]
        [id = #1, prev = #3, next = #4, val = C]
        [id = #4, prev = #1, next = #0, val = D]
        >>> ll.reverse()
        >>> ll
        first = #4, last = #1
        [id = #4, prev = #0, next = #3, val = D]
        [id = #3, prev = #4, next = #2, val = C]
        [id = #2, prev = #3, next = #1, val = B]
        [id = #1, prev = #2, next = #0, val = A]

        >>> ll = LinkedList()
        >>> ll
        first = #0, last = #0
        >>> ll.reverse()
        >>> ll
        first = #0, last = #0
        """
        # If list is empty, I swear, didn't du nuthin
        if self.first is None:
            return
        reversed_list = LinkedList()
        next_item = self.first
        next_item_before = None
        # we want our item ids to start with 1 again, so set to 0
        LinkedListItem.num_items = 0
        # iterate over all items and add them in reverse order to reversed_list
        while next_item is not None:
            new_item = LinkedListItem(next_item.value)
            reversed_list.insert_before(new_item, next_item_before)
            next_item_before, next_item = [new_item, next_item.next]
        # overwrite self.first and self.last with properties of reversed_list
        # so that our changes take effect
        self.first, self.last = [reversed_list.first, reversed_list.last]

    def splice(self, l1, l2):
        """
        Cut out the segment given by l1 and l2 and return it as a new
        LinkedList. l1 and l2 are always contained in the linked list and l1
        is always before l2.

        >>> LinkedListItem.num_items = 0
        >>> ll = LinkedList()
        >>> item_C = LinkedListItem('C')
        >>> item_A = LinkedListItem('A')
        >>> item_B = LinkedListItem('B')
        >>> item_D = LinkedListItem('D')
        >>> ll.insert_before(item_C, None)
        >>> ll.insert_before(item_A, item_C)
        >>> ll.insert_before(item_B, item_C)
        >>> ll.insert_before(item_D, None)
        >>> ll
        first = #2, last = #4
        [id = #2, prev = #0, next = #3, val = A]
        [id = #3, prev = #2, next = #1, val = B]
        [id = #1, prev = #3, next = #4, val = C]
        [id = #4, prev = #1, next = #0, val = D]
        >>> ll.splice(item_B, item_C)
        first = #3, last = #1
        [id = #3, prev = #0, next = #1, val = B]
        [id = #1, prev = #3, next = #0, val = C]
        >>> ll
        first = #2, last = #4
        [id = #2, prev = #0, next = #4, val = A]
        [id = #4, prev = #2, next = #0, val = D]
        >>> ll.splice(item_A, item_D)
        first = #2, last = #4
        [id = #2, prev = #0, next = #4, val = A]
        [id = #4, prev = #2, next = #0, val = D]
        >>> ll
        first = #0, last = #0
        """
        # If the element before l1 is not None, l1 is not the first
        # element in list, so set the pointer of previous
        # element to the element after l2
        if l1.prev is not None:
            l1.prev.next = l2.next
        else:
            # If first element was l1, set it to the element after l2
            self.first = l2.next

        # If l2 is not last element, set the pointer of next element to
        # the element before l1
        if l2.next is not None:
            l2.next.prev = l1.prev
        else:
            # if last element was l2, set it to the element before l1
            self.last = l1.prev

        # In our sliced list there is nothing before first or after last
        # element
        l1.prev = l2.next = None

        # Create a new LinkedList and set first and last element to mutated
        # l1 and l2
        part_list = LinkedList()
        part_list.first, part_list.last = [l1, l2]
        return part_list


class LinkedListItem:
    """
    A single item from a linked list.

    >>> LinkedListItem.num_items = 0
    >>> LinkedListItem('A')
    [id = #1, prev = #0, next = #0, val = A]
    """

    num_items = 0

    def __init__(self, value):
        """ Construct an item with given value. Also have an id for each item,
        so that we can simply show pointers as ids. """

        LinkedListItem.num_items += 1
        self.id = LinkedListItem.num_items
        self.prev = None
        self.next = None
        self.value = value

    def __repr__(self):
        """ Item as human-readable string. In Java or C++, use a function like
        toString(). """

        return "[id = #" + str(self.id) \
            + ", prev = #" + str(0 if self.prev is None else self.prev.id) \
            + ", next = #" + str(0 if self.next is None else self.next.id) \
            + ", val = " + str(self.value) + "]"
