import threading
from abc import ABCMeta


class SingletonMeta(type):
    """
    A metaclass that ensures only one instance of a class is created (singleton pattern).
    This is thread-safe due to the use of a lock.
    """

    _instances = {}  # Dictionary to store instances of singleton classes.
    _lock = threading.Lock()  # Lock to ensure thread-safe instantiation.

    def __call__(cls, *args, **kwargs):
        """
        Overrides the default __call__ method to ensure only one instance of the class is created.
        """
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonABCMeta(ABCMeta, SingletonMeta):
    """
    A metaclass that combines the features of ABCMeta (for abstract base classes)
    and SingletonMeta (for singleton behaviour).
    """

    pass
