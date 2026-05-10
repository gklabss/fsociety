import os
import hashlib
import requests
from datetime import datetime

class AntivirusScanner:
    def __init__(self):
        # Known malware signatures (in a real implementation, this would be extensive)
        self.malware_signatures = {
            "eicar_test": "44d88612fea8a8f36de82e1278abb02f",  # EICAR test signature
        }
        self.scan_log = []

    def scan_file(self, file_path):
        """Scan a single file for malware signatures"""
        if not os.path.exists(file_path):
            return {"status": "error", "message": "File not found"}

        try:
            # Calculate file hash
            file_hash = self._calculate_file_hash(file_path)

            # Check against known signatures
            if file_hash in self.malware_signatures.values():
                threat_name = self._get_threat_name(file_hash)
                result = {
                    "status": "infected",
                    "file": file_path,
                    "threat": threat_name,
                    "hash": file_hash,
                    "timestamp": datetime.now().isoformat()
                }
                self.scan_log.append(result)
                return result
            else:
                result = {
                    "status": "clean",
                    "file": file_path,
                    "hash": file_hash,
                    "timestamp": datetime.now().isoformat()
                }
                self.scan_log.append(result)
                return result

        except Exception as e:
            return {"status": "error", "message": str(e)}

    def scan_directory(self, directory_path):
        """Scan all files in a directory"""
        results = []
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                result = self.scan_file(file_path)
                results.append(result)
        return results

    def _calculate_file_hash(self, file_path):
        """Calculate MD5 hash of a file"""
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def _get_threat_name(self, file_hash):
        """Get threat name from hash"""
        for name, signature in self.malware_signatures.items():
            if signature == file_hash:
                return name
        return "Unknown"

    def quarantine_file(self, file_path, quarantine_dir="quarantine"):
        """Move infected file to quarantine directory"""
        if not os.path.exists(quarantine_dir):
            os.makedirs(quarantine_dir)

        try:
            filename = os.path.basename(file_path)
            quarantine_path = os.path.join(quarantine_dir, filename)

            # Move file to quarantine
            os.rename(file_path, quarantine_path)

            return {
                "status": "quarantined",
                "original_path": file_path,
                "quarantine_path": quarantine_path
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def update_signatures(self):
        """Update malware signatures from online database"""
        # In a real implementation, this would connect to a signature database
        return {"status": "success", "message": "Signatures are up to date"}

def create_scanner():
    """Factory function to create antivirus scanner instance"""
    return AntivirusScanner()