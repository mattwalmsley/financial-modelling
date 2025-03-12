# Python Logging

## Example Singleton Logger

```python
import logging
import logging.handlers
import os
import threading
import time
from abc import ABCMeta, abstractmethod
from datetime import datetime, timedelta


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


class BaseLogger(metaclass=SingletonABCMeta):
    """
    An abstract base class for logging. Ensures that subclasses implement the required logging methods.
    This class also enforces singleton behaviour.
    """

    @abstractmethod
    def debug(self, message: str):
        """
        Log a debug-level message.

        Args:
            message (str): The message to log.
        """
        pass

    @abstractmethod
    def info(self, message: str):
        """
        Log an info-level message.

        Args:
            message (str): The message to log.
        """
        pass

    @abstractmethod
    def warning(self, message: str):
        """
        Log a warning-level message.

        Args:
            message (str): The message to log.
        """
        pass

    @abstractmethod
    def error(self, message: str):
        """
        Log an error-level message.

        Args:
            message (str): The message to log.
        """
        pass

    @abstractmethod
    def critical(self, message: str):
        """
        Log a critical-level message.

        Args:
            message (str): The message to log.
        """
        pass


class Logger(BaseLogger):
    """
    A concrete implementation of the BaseLogger class. This logger supports log file rolling
    on application start and automatic cleanup of old log files based on a specified retention period.

    Log files are stored in a 'logs' directory.
    """

    def __init__(self, log_file='log_file.log', cleanup_days=30):
        """
        Initialize the logger.

        Args:
            log_file (str): The name of the log file. Defaults to 'log_file.log'.
            cleanup_days (int): The number of days to retain log files. Defaults to 30.
        """

        # Ensure the 'logs' directory exists
        self._log_dir = 'logs'
        os.makedirs(self._log_dir, exist_ok=True)

        # Set the full path for the log file
        self._log_file = os.path.join(self._log_dir, log_file)

        # Initialize the logger
        self._logger = logging.getLogger('logger')
        self._logger.setLevel(logging.DEBUG)

        # Roll over log file on application start
        if os.path.exists(self._log_file):
            os.rename(self._log_file, f"{self._log_file}.{datetime.now().strftime('%Y%m%d%H%M%S')}")

        # Create a file handler with rolling based on time
        self.file_handler = logging.handlers.TimedRotatingFileHandler(
            self._log_file, when='midnight', interval=1, backupCount=cleanup_days
        )
        self.file_handler.setLevel(logging.DEBUG)

        # Create a console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Define the log message format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add the handlers to the logger
        self._logger.addHandler(self.file_handler)
        self._logger.addHandler(console_handler)

        # Schedule log file cleanup
        self._cleanup_days = cleanup_days
        self._schedule_cleanup()

    def _schedule_cleanup(self):
        """
        Schedule a background thread to clean up old log files based on the retention period.
        """

        def cleanup():
            """
            Continuously check for and delete log files older than the specified retention period.
            """
            while True:
                now = datetime.now()
                cutoff = now - timedelta(days=self._cleanup_days)
                for handler in self._logger.handlers:
                    if isinstance(handler, logging.handlers.TimedRotatingFileHandler):
                        for filename in os.listdir(self._log_dir):
                            if filename.startswith(os.path.basename(handler.baseFilename)):
                                filepath = os.path.join(self._log_dir, filename)
                                file_creation_time = datetime.fromtimestamp(os.path.getctime(filepath))
                                if file_creation_time < cutoff:
                                    os.remove(filepath)
                time.sleep(86400)  # Sleep for 24 hours

        cleanup_thread = threading.Thread(target=cleanup, daemon=True)
        cleanup_thread.start()

    def debug(self, message: str):
        """
        Log a debug-level message.

        Args:
            message (str): The message to log.
        """
        self._logger.debug(message)

    def info(self, message: str):
        """
        Log an info-level message.

        Args:
            message (str): The message to log.
        """
        self._logger.info(message)

    def warning(self, message: str):
        """
        Log a warning-level message.

        Args:
            message (str): The message to log.
        """
        self._logger.warning(message)

    def error(self, message: str):
        """
        Log an error-level message.

        Args:
            message (str): The message to log.
        """
        self._logger.error(message)

    def critical(self, message: str):
        """
        Log a critical-level message.

        Args:
            message (str): The message to log.
        """
        self._logger.critical(message)

# Example usage
logger = Logger(cleanup_days=30)
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

uvicorn_logger = logging.getLogger("uvicorn")
uvicorn_logger.addHandler(logger.file_handler)  # Reuse the same file handler
```
