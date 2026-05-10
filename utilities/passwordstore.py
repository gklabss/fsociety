import hashlib
import json
import os
from cryptography.fernet import Fernet

class PasswordManager:
    def __init__(self, master_password=None):
        self.passwords = {}
        self.key = self._generate_key(master_password) if master_password else Fernet.generate_key()
        self.cipher = Fernet(self.key)
        self.storage_file = "passwords.enc"

    def _generate_key(self, master_password):
        """Generate encryption key from master password"""
        return hashlib.sha256(master_password.encode()).digest()

    def add_password(self, service, username, password):
        """Add a password to the vault"""
        # Encrypt the password
        encrypted_password = self.cipher.encrypt(password.encode())

        # Store the encrypted password
        if service not in self.passwords:
            self.passwords[service] = {}

        self.passwords[service][username] = encrypted_password.decode()
        return True

    def get_password(self, service, username):
        """Retrieve a password from the vault"""
        if service in self.passwords and username in self.passwords[service]:
            encrypted_password = self.passwords[service][username].encode()
            decrypted_password = self.cipher.decrypt(encrypted_password)
            return decrypted_password.decode()
        return None

    def delete_password(self, service, username):
        """Delete a password from the vault"""
        if service in self.passwords and username in self.passwords[service]:
            del self.passwords[service][username]
            return True
        return False

    def list_services(self):
        """List all services in the vault"""
        return list(self.passwords.keys())

    def save_to_file(self, filename=None):
        """Save passwords to encrypted file"""
        file_path = filename or self.storage_file
        data = {
            "passwords": self.passwords,
            "key": self.key.decode()
        }
        with open(file_path, 'w') as f:
            json.dump(data, f)
        return True

    def load_from_file(self, filename=None):
        """Load passwords from encrypted file"""
        file_path = filename or self.storage_file
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                data = json.load(f)
                self.passwords = data["passwords"]
                self.key = data["key"].encode()
                self.cipher = Fernet(self.key)
            return True
        return False

    def generate_password(self, length=12):
        """Generate a strong password"""
        import random
        import string
        characters = string.ascii_letters + string.digits + "!@#$%^&*"
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

def create_password_manager(master_password=None):
    """Factory function to create password manager instance"""
    return PasswordManager(master_password)