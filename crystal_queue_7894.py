class Crystal:
    """
    A simple queue management class.
    """

    def __init__(self):
        """
        Initializes an empty queue.
        """
        self._queue = []

    def enqueue(self, item):
        """
        Adds an item to the end of the queue.

        Args:
            item: The item to add.
        """
        self._queue.append(item)

    def dequeue(self):
        """
        Removes and returns the item from the front of the queue.

        Returns:
            The item that was at the front of the queue, or None if the queue is empty.
        """
        if not self.is_empty():
            return self._queue.pop(0)
        return None

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            True if the queue is empty, False otherwise.
        """
        return len(self._queue) == 0

    def size(self):
        """
        Returns the number of items in the queue.

        Returns:
            The size of the queue.
        """
        return len(self._queue)

    def peek(self):
        """
        Returns the item at the front of the queue without removing it.

        Returns:
            The item at the front of the queue, or None if the queue is empty.
        """
        if not self.is_empty():
            return self._queue[0]
        return None


# Example usage:
if __name__ == "__main__":
    crystal_queue = Crystal()
    crystal_queue.enqueue("First")
    crystal_queue.enqueue("Second")
    print(f"Size: {crystal_queue.size()}")  # Size: 2
    print(f"Peek: {crystal_queue.peek()}")  # Peek: First
    item = crystal_queue.dequeue()
    print(f"Dequeued: {item}")  # Dequeued: First
    print(f"Empty? {crystal_queue.is_empty()}")  # Empty? False