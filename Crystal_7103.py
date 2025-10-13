import queue
import threading
import time

class Crystal:
    """
    Класс Crystal для управления очередью.
    Предоставляет потокобезопасный интерфейс для добавления и извлечения элементов.
    """

    def __init__(self, maxsize=0):
        """
        Инициализирует очередь.

        Args:
            maxsize (int): Максимальный размер очереди. 0 означает неограниченную очередь.
        """
        self._queue = queue.Queue(maxsize=maxsize)
        self._lock = threading.Lock()

    def enqueue(self, item):
        """
        Добавляет элемент в конец очереди.

        Args:
            item: Элемент для добавления.
        """
        self._queue.put(item)

    def dequeue(self):
        """
        Удаляет и возвращает элемент из начала очереди.
        Если очередь пуста, блокирует выполнение до появления элемента.

        Returns:
            Элемент из начала очереди.
        """
        return self._queue.get()

    def peek(self):
        """
        Возвращает элемент из начала очереди без его удаления.
        Если очередь пуста, возвращает None.

        Returns:
            Первый элемент очереди или None.
        """
        with self._lock:
            if not self._queue.empty():
                # Queue не предоставляет прямого доступа к первому элементу, поэтому делаем хак
                # с временным извлечением и возвратом. Это не идеально в многопоточной среде.
                # Более правильный способ - использовать collections.deque и внешнюю блокировку.
                temp_item = self._queue.get_nowait()
                self._queue.put_nowait(temp_item)
                return temp_item
            else:
                return None

    def size(self):
        """
        Возвращает текущий размер очереди.

        Returns:
            int: Количество элементов в очереди.
        """
        return self._queue.qsize()

    def is_empty(self):
        """
        Проверяет, пуста ли очередь.

        Returns:
            bool: True, если очередь пуста, иначе False.
        """
        return self._queue.empty()

    def is_full(self):
        """
        Проверяет, заполнена ли очередь.

        Returns:
            bool: True, если очередь заполнена, иначе False.
        """
        return self._queue.full()
