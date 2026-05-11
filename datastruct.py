"""datastruct.py

# Data Structures

This module defines the LinkedList abstract data type
"""
############################### 72 chars ###############################


class Node:
    """Represents a node in a linkedlist.

    Arguments
        - data
          The data encapsulated in the node.

    Attributes
        - next: Node | None
          The next node in the linkedlist, or None if the node is the tail.

    Methods
        - get() -> data
          Return the data stored in the node.
    """

    def __init__(self, data: tuple[int, int]):
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return f'Node({self.get()})'

    def get(self) -> tuple[int, int]:
        """Return the data stored in the node.

        Arguments
            None

        Return
            tuple[int, int]
        """
        return self.data


class LinkedList:
    """Represents a sequence of data items.

    Arguments
        None

    Attributes
        None

    Methods
        - length() -> int
        - get(index) -> item
        - insert(index, item) -> None
        - append(item) -> None
        - delete(index) -> None
    """

    def __init__(self):
        self._head = None

    def __repr__(self) -> str:
        return 'LinkedList()'

    def length(self) -> int:
        """Returns the number of nodes in the linkedlist.

        Arguments
            None

        Return
            length of linkedlist as an integer (zero or positive)
        """
        # no need to check if the start is none because it tallies
        current_node = self._head
        counter = 0
        while current_node != None:
            current_node = current_node.next
            counter += 1
        return counter

    def get(self, n: int) -> tuple[int, int]:
        """Returns item at n-th node.

        Arguments
            - n: int
              sequence number of item to be retrieved.

        Returns
            item

        Raises
            IndexError if n >= length
        """
        if n >= self.length():
            raise IndexError
        current_node = self._head
        for i in range(n):
            current_node = current_node.next
        return current_node.get()

    def insert(self, n: int, item: tuple[int, int]) -> None:
        """Insert item into linkedlist at position n.

        If n == 0, inserts item at the head.
        If n == length, appends item at the tail of the linkedlist.

        Arguments
            - n: int
              sequence number of item to be inserted.

        Raises
            IndexError if n > length
        """
        # n will be the index of the node in the list
        current_node = self._head
        # special case: if n == 0
        if n == 0:
            new_node = Node(item)
            new_node.next = self._head
            self._head = new_node
        elif n > self.length():
            raise IndexError
        else:
        # for all other cases
            for i in range(n-1):
                current_node = current_node.next
            new_node = Node(item)
            new_node.next = current_node.next
            current_node.next = new_node
            
    def append(self, item: tuple[int, int]) -> None:
        """Append item at the end of linkedlist.

        Arguments
            - item
              The item to be appended.

        Returns
            None
        """
        # check if node is empty
        # only loop if self._head is not None, if not current_node.next will raise an error
        # finally, connect it to the node created with the item parameter
        if self._head == None:
            self._head = Node(item)
        else:
            current_node = self._head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = Node(item)

    def delete(self, n: int) -> None:
        """Delete n-th item from linkedlist.

        Arguments
            - n: int
              sequence number of item to be retrieved.

        Raises
            IndexError if n > length
        """
        # Replace the line below with your code
        if n > self.length():
            raise IndexError("n must be 0 or positive")

        previous_node = self._head
        # If n == 0
        if n == 0:
            self._head = previous_node.next
            # then python automatically frees previous_node
        else:
            for i in range(n - 1):
                previous_node = previous_node.next
            current_node = previous_node.next
            previous_node.next = current_node.next
            # then python automatically frees current_node
       
    def contains(self, item: tuple[int, int]) -> bool:
        """Checks whether an item is in the linkedlist.
        Returns a boolean value to indicate the status of the search.

        Arguments
            - item
              The item to be searched for.

        Returns
            True if item is found in the linkedlist,
            otherwise False
        """
        # Set current node to the head
        current_node = self._head
        
        while current_node != None:
            # check if data in node equals to item
            if current_node.get() == item:
                return True
            else:
                current_node = current_node.next
        
        # reached the end
        return False


if __name__ == "__main__":
    # Write any test code here and run it with
    # `python datastruct.py`
    pass
