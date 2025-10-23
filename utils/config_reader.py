"""
Configuration Reader
Reads configuration from environment variables and .env file
"""
import os
from pathlib import Path
from dotenv import load_dotenv


class ConfigReader:
    """Singleton configuration reader"""

    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not ConfigReader._initialized:
            # Load environment variables from .env file
            env_path = Path(__file__).parent.parent / ".env"
            load_dotenv(env_path)
            ConfigReader._initialized = True

    @property
    def base_url(self) -> str:
        """Get base URL"""
        return os.getenv("BASE_URL", "https://ultimateqa.com/automation")

    @property
    def browser(self) -> str:
        """Get browser type"""
        return os.getenv("BROWSER", "chromium")

    @property
    def headless(self) -> bool:
        """Get headless mode"""
        return os.getenv("HEADLESS", "false").lower() == "true"

    @property
    def timeout(self) -> int:
        """Get default timeout in milliseconds"""
        return int(os.getenv("TIMEOUT", "30000"))

    @property
    def slow_mo(self) -> int:
        """Get slow motion delay"""
        return int(os.getenv("SLOW_MO", "0"))

    @property
    def screenshot_on_failure(self) -> bool:
        """Get screenshot on failure setting"""
        return os.getenv("SCREENSHOT_ON_FAILURE", "true").lower() == "true"

    @property
    def trace_on_failure(self) -> bool:
        """Get trace on failure setting"""
        return os.getenv("TRACE_ON_FAILURE", "true").lower() == "true"

    @property
    def video_on_failure(self) -> bool:
        """Get video on failure setting"""
        return os.getenv("VIDEO_ON_FAILURE", "false").lower() == "true"

    @property
    def parallel_workers(self) -> int:
        """Get number of parallel workers"""
        return int(os.getenv("PARALLEL_WORKERS", "1"))


# Global config instance
config = ConfigReader()
