"""cq.py

# Circular Queue

This module defines the CircularQueue data type
"""
############################### 72 chars ###############################


class CircularQueue:
    """Circular Queue implemented as Array.

    Methods
        - enqueue(item)
          Adds item at the end of the queue.

        - dequeue()
          Returns the first item in the queue.
    """

    def __init__(self, size: int):
        self.size = size
        self._data = [None] * size
        self.head = None  # points at first element, sentinel value is None when queue is empty
        self.tail = 0  # points at first empty element

    def __repr__(self) -> str:
        return f"CircularQueue({self.size})"

    def enqueue(self, item: tuple[int, int]) -> None:
        """Add item at the end of the queue.

        Arguments
            - item
              The item to be added.

        Return
            None
        """
        if self.head == self.tail:
            print("queue is full")
            return False
        if self.head == None:
            self.head = 0
        self._data[self.tail] = item
        self.tail += 1
        if self.tail == self.size:
            self.tail = 0

    def dequeue(self) -> tuple[int, int]:
        """Return the item at the head of the queue.

        Arguments
            None

        Return
            item
        """
        # Delete the line below and write your code here
        if self.head == None:
            print("queue is empty")
            return False
        item = self._data[self.head]
        self.head += 1
        if self.head == self.size:
            self.head = 0
        if self.head == self.tail:
            self.head = None
            self.tail = 0
        return item


if __name__ == "__main__":
    # Write any test code here and run it with
    # `python cq.py`
    cq = CircularQueue(3)
    # breakpoint()
    for k in range(2):
        for i in range(4):
            cq.enqueue((i, i*i))
        for i in range(4):
            print(cq.dequeue())
