"""
A class to manage a queue of items, representing 'crystals'.
It supports adding (enqueueing), removing (dequeueing),
checking the size, and getting a string representation.
"""

class Crystal:
    """
    A simple queue-like class for managing a collection of items.
    """

    def __init__(self):
        """Initializes the Crystal with an empty list."""
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

    def size(self):
        """
        Returns the number of items in the queue.

        Returns:
            The integer count of items.
        """
        return len(self._queue)

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            True if the queue is empty, False otherwise.
        """
        return len(self._queue) == 0

    def __str__(self):
        """
        Provides a string representation of the queue.

        Returns:
            A string showing the items in the queue.
        """
        return f"Crystal Queue: {self._queue}"

# Example usage:
if __name__ == "__main__":
    crystal = Crystal()
    crystal.enqueue("Amethyst")
    crystal.enqueue("Topaz")
    print(crystal)
    print(f"Size: {crystal.size()}")
    item = crystal.dequeue()
    print(f"Dequeued: {item}")
    print(crystal)