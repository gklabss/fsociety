import socket
import subprocess
import platform

class VulnerabilityScanner:
    def __init__(self):
        self.vulnerabilities_found = []

    def scan_port(self, target, port):
        """Scan a single port on the target"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            sock.close()
            return result == 0  # 0 means port is open
        except:
            return False

    def scan_ports(self, target, port_range=(1, 1000)):
        """Scan a range of ports on the target"""
        open_ports = []
        start_port, end_port = port_range

        for port in range(start_port, end_port + 1):
            if self.scan_port(target, port):
                open_ports.append(port)

        return {
            "open_ports": open_ports,
            "total_found": len(open_ports)
        }

    def check_service(self, target, port):
        """Check what service is running on a specific port"""
        try:
            service = socket.getservbyport(port)
            return service
        except:
            return "Unknown service"

    def scan_vulnerabilities(self, target):
        """Scan for common system vulnerabilities"""
        vulnerabilities = []

        # Check for open ports
        common_ports = [21, 22, 23, 25, 80, 110, 143, 443, 3389, 5432, 3306]
        open_ports = []

        for port in common_ports:
            if self.scan_port(target, port):
                service = self.check_service(target, port)
                vulnerabilities.append({
                    "port": port,
                    "service": service,
                    "status": "OPEN"
                })
                open_ports.append(port)

        return {
            "open_ports": open_ports,
            "vulnerabilities": vulnerabilities
        }

def create_vulnerability_scanner():
    """Factory function to create vulnerability scanner instance"""
    return VulnerabilityScanner()