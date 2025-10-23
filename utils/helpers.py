"""
Helper Utilities
Common helper functions for test automation
"""
import time
from pathlib import Path
from datetime import datetime
from typing import Callable, Any


def create_directory(dir_name: str) -> Path:
    """
    Create directory if it doesn't exist

    Args:
        dir_name: Directory name

    Returns:
        Path object
    """
    directory = Path(dir_name)
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def get_timestamp(format_string: str = "%Y%m%d_%H%M%S") -> str:
    """
    Get current timestamp

    Args:
        format_string: Timestamp format

    Returns:
        Formatted timestamp string
    """
    return datetime.now().strftime(format_string)


def wait_for_condition(
    condition: Callable[[], bool],
    timeout: int = 30,
    poll_interval: float = 0.5,
    error_message: str = "Condition not met within timeout"
) -> bool:
    """
    Wait for a condition to be true

    Args:
        condition: Function that returns boolean
        timeout: Maximum time to wait in seconds
        poll_interval: Time between checks in seconds
        error_message: Error message if timeout

    Returns:
        True if condition met

    Raises:
        TimeoutError: If condition not met within timeout
    """
    end_time = time.time() + timeout
    while time.time() < end_time:
        if condition():
            return True
        time.sleep(poll_interval)
    raise TimeoutError(error_message)


def retry_on_exception(
    func: Callable,
    max_attempts: int = 3,
    delay: float = 1.0,
    exceptions: tuple = (Exception,)
) -> Any:
    """
    Retry function on exception

    Args:
        func: Function to retry
        max_attempts: Maximum number of attempts
        delay: Delay between attempts in seconds
        exceptions: Tuple of exceptions to catch

    Returns:
        Function result

    Raises:
        Last exception if all attempts fail
    """
    last_exception = None
    for attempt in range(max_attempts):
        try:
            return func()
        except exceptions as e:
            last_exception = e
            if attempt < max_attempts - 1:
                time.sleep(delay)
    raise last_exception  # type: ignore


def sanitize_filename(filename: str) -> str:
    """
    Sanitize filename by removing invalid characters

    Args:
        filename: Original filename

    Returns:
        Sanitized filename
    """
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename


def get_project_root() -> Path:
    """
    Get project root directory

    Returns:
        Path to project root
    """
    return Path(__file__).parent.parent


def read_file(file_path: str | Path) -> str:
    """
    Read file content

    Args:
        file_path: Path to file

    Returns:
        File content as string
    """
    with open(file_path, encoding='utf-8') as f:
        return f.read()


def write_file(file_path: str | Path, content: str) -> None:
    """
    Write content to file

    Args:
        file_path: Path to file
        content: Content to write
    """
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
