from linked_list import LinkedList, LinkedListItem


class BucketQueue:
    def __init__(self, m):
        """
        >>> bq = BucketQueue(10)
        >>> bq.min is False
        True
        >>> len(bq.bq)
        10
        """
        self.bq = [None] * m
        self.min = False

    def insert(self, key, value):
        """
        >>> bq = BucketQueue(43)
        >>> bq.min
        False
        >>> num_items_before = LinkedListItem.num_items
        >>> item42a = bq.insert(42, "fourtytwo")
        >>> bq.bq[42].first.value
        'fourtytwo'
        >>> bq.min
        42
        >>> item42b = bq.insert(42, 'zweiundvierzig')
        >>> bq.bq[42].first.next.value
        'zweiundvierzig'
        >>> bq.min
        42
        >>> item1a = bq.insert(1, 'eins')
        >>> bq.min
        1
        """

        # create new linkedlistitem
        item = LinkedListItem(key, value)
        self._insert(key, item)
        return item

    def _insert(self, key, item):
        if self.bq[key] is None:
            self.bq[key] = LinkedList()

        self.bq[key].insert_before(item, None)

        # if key is smaller than self.min, update it
        if key < self.min or self.min is False:
            self.min = key

    def get_min(self):
        """
        >>> bq = BucketQueue(11)
        >>> bq.get_min()
        Traceback (most recent call last):
          ...
        Exception: BucketQueue is empty
        >>> item9a = bq.insert(9, 'neun')
        >>> item10a = bq.insert(10, 'dix')
        >>> bq.get_min() == item9a
        True
        >>> item2a = bq.insert(2, 'deux')
        >>> bq.get_min() == item2a
        True
        """
        if self.min is False:
            raise Exception('BucketQueue is empty')
        return self.bq[self.min].first

    def delete_min(self):
        """
        >>> bq = BucketQueue(10)
        >>> item1a = bq.insert(1, "eins")
        >>> item1b = bq.insert(1, "one")
        >>> item2a = bq.insert(2, "deux")
        >>> item8a = bq.insert(8, "eight")
        >>> bq.min
        1
        >>> bq.get_min() == item1a
        True
        >>> bq.delete_min()
        >>> bq.min
        1
        >>> bq.get_min() == item1b
        True
        >>> bq.delete_min()
        >>> bq.min
        2
        >>> bq.get_min() == item2a
        True
        >>> bq.delete_min()
        >>> bq.min
        8
        >>> bq.get_min() == item8a
        True
        >>> bq.delete_min()
        >>> bq.min
        False
        """
        if self.min is False:
            raise Exception("BucketQueue is empty")

        first_item = self.bq[self.min].first
        self.bq[self.min].remove(first_item)

        # Update self.min to the key where linkedlist is not empty, if possible
        if self.bq[self.min].first is None:
            # was last item in linked list, now we have to find the first
            # linked list which is not empty
            self.min = False
            for m in range(0, len(self.bq)):
                if self.bq[m] is not None and self.bq[m].first is not None:
                    self.min = m
                    break

    def change_key(self, item, new_key):
        """
        >>> bq = BucketQueue(10)
        >>> item1a = bq.insert(1, "eins")
        >>> item1b = bq.insert(1, "one")
        >>> item4a = bq.insert(1, "fyrta")
        >>> item2a = bq.insert(2, "deux")
        >>> item8a = bq.insert(8, "eight")
        >>> bq.bq[1].last == item4a
        True
        >>> item4a.key
        1
        >>> bq.change_key(item4a, 4)
        >>> item4a.key
        4
        >>> bq.bq[1].last == item1b
        True
        >>> bq.bq[4].first == item4a
        True
        """
        # Check if item is first in linkedlist
        if item.prev is None:
            # if so, find the correct linked list and change first to item.next
            for m in range(0, len(self.bq)):
                if self.bq[m] is not None and self.bq[m].first == item:
                    self.bq[m].first = self.bq[m].first.next
                    break

        # Check if item is last in linkedlist
        if item.next is None:
            # if so, find the correct linked list and change last to item.prev
            for m in range(0, len(self.bq)):
                if self.bq[m] is not None and self.bq[m].last == item:
                    self.bq[m].last = self.bq[m].last.prev
                    break

        # Now perform a splice without knowing the linkedlist
        if item.prev is not None:
            item.prev.next = item.next
            item.prev = None
        if item.next is not None:
            item.next.prev = item.prev
            item.next = None

        # Don't forget changing the key of LinkedListItem
        item.key = new_key

        # and finally, insert
        self._insert(new_key, item)
