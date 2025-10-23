"""
Test Data Management
Handles test data generation and loading
"""
import json
import yaml
from pathlib import Path
from faker import Faker


fake = Faker()


class TestDataManager:
    """Manages test data from various sources"""

    @staticmethod
    def load_json(file_path: str) -> dict:
        """
        Load data from JSON file

        Args:
            file_path: Path to JSON file

        Returns:
            Dictionary with loaded data
        """
        with open(file_path, encoding='utf-8') as f:
            return json.load(f)

    @staticmethod
    def load_yaml(file_path: str) -> dict:
        """
        Load data from YAML file

        Args:
            file_path: Path to YAML file

        Returns:
            Dictionary with loaded data
        """
        with open(file_path, encoding='utf-8') as f:
            return yaml.safe_load(f)

    @staticmethod
    def save_json(data: dict, file_path: str) -> None:
        """
        Save data to JSON file

        Args:
            data: Data to save
            file_path: Path to JSON file
        """
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)


class ContactFormData:
    """Test data for contact form"""

    @staticmethod
    def get_valid_data() -> dict:
        """
        Get valid contact form data

        Returns:
            Dictionary with valid test data
        """
        return {
            "name": fake.name(),
            "message": fake.text(max_nb_chars=200)
        }

    @staticmethod
    def get_invalid_name_data() -> dict:
        """
        Get data with invalid name

        Returns:
            Dictionary with invalid name data
        """
        return {
            "name": "",  # Empty name
            "message": fake.text(max_nb_chars=200)
        }

    @staticmethod
    def get_invalid_message_data() -> dict:
        """
        Get data with invalid message

        Returns:
            Dictionary with invalid message data
        """
        return {
            "name": fake.name(),
            "message": ""  # Empty message
        }

    @staticmethod
    def get_boundary_data() -> dict:
        """
        Get boundary test data

        Returns:
            Dictionary with boundary test data
        """
        return {
            "name": "A" * 100,  # Very long name
            "message": fake.text(max_nb_chars=5000)  # Very long message
        }

    @staticmethod
    def get_special_characters_data() -> dict:
        """
        Get data with special characters

        Returns:
            Dictionary with special characters
        """
        return {
            "name": "Test!@#$%^&*()",
            "message": "Special chars: <>&\"'{}[]|\\`~"
        }


class UserData:
    """Test data for user information"""

    @staticmethod
    def get_random_user() -> dict:
        """
        Get random user data

        Returns:
            Dictionary with user data
        """
        return {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "phone": fake.phone_number(),
            "address": fake.address(),
            "company": fake.company(),
            "job_title": fake.job()
        }

    @staticmethod
    def get_multiple_users(count: int = 5) -> list:
        """
        Get multiple random users

        Args:
            count: Number of users to generate

        Returns:
            List of user dictionaries
        """
        return [UserData.get_random_user() for _ in range(count)]
