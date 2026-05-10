#imports
from attack.dos import dos_attack
from attack.ddos import ddos_attack
from defense.proxy import ProxyServer
from defense.antivirus import AntivirusScanner
from utilities.passwordstore import PasswordManager
from utilities.vulnscanner import VulnerabilityScanner
from socialengineering.email import SocialEngineeringEmail

#start
print("*---------------------------------------------------------------*")
print('|                welcome to fsocitey                            |')
print("*---------------------------------------------------------------*")

print("Available modules :-")
print("(1). DOS attack")
print("(2). DDoS attack")
print("(3). Vulnerability Scanner (Utilities)")
print("(4). Proxy Server (Defense)")
print("(5). Antivirus Scanner (Defense)")
print("(6). Password Manager (Utilities)")
print("(7). Social Engineering Email (Social Engineering)")
print("(8). Quit")
print("Note: Type the numbers to select an option\n")

# Initialize modules
proxy_server = None
antivirus_scanner = AntivirusScanner()
password_manager = PasswordManager()
vuln_scanner = VulnerabilityScanner()
social_engineering_tool = SocialEngineeringEmail()

#main-code
while True:
    command = input('command-> ')
    if command == "1":
        url = input("Type the URL for the Attack (don't leave empty): ")
        if not url:
            print("URL cannot be empty!")
            continue
        power = input("Type the amount of requests (1-100): ")
        try:
            power = int(power)
        except ValueError:
            power = 10  # Default to 10 if invalid input
            print("Invalid power input, using default value of 10")
        result = dos_attack(url, power)
        print(f"Result: {result}")
    elif command == "2":
        url = input("Type the URL for the Attack (don't leave empty): ")
        if not url:
            print("URL cannot be empty!")
            continue
        power = input("Type the amount of requests (1-50): ")
        try:
            power = int(power)
        except ValueError:
            power = 10  # Default to 10 if invalid input
            print("Invalid power input, using default value of 10")
        result = ddos_attack(url, power)
        print(f"Result: {result}")
    elif command == "3":
        print("Vulnerability Scanner")
        target = input("Enter target IP or hostname: ")
        if target:
            result = vuln_scanner.scan_vulnerabilities(target)
            print(f"Scan results: {result}")
        else:
            print("Invalid target")
    elif command == "4":
        print("Proxy Server")
        print("(1) Start Proxy Server")
        print("(2) Stop Proxy Server")
        proxy_choice = input("Select option: ")
        if proxy_choice == "1":
            port = input("Enter port (default 8080): ")
            try:
                port = int(port) if port else 8080
            except ValueError:
                port = 8080
            proxy_server = ProxyServer(port=port)
            result = proxy_server.start()
            if result:
                print(f"Proxy server started on port {port}")
            else:
                print("Failed to start proxy server")
        elif proxy_choice == "2" and proxy_server:
            proxy_server.stop()
            print("Proxy server stopped")
        else:
            print("Proxy server not running")
    elif command == "5":
        print("Antivirus Scanner")
        print("(1) Scan File")
        print("(2) Scan Directory")
        print("(3) Update Signatures")
        av_choice = input("Select option: ")
        if av_choice == "1":
            file_path = input("Enter file path: ")
            if file_path:
                result = antivirus_scanner.scan_file(file_path)
                print(f"Scan result: {result}")
        elif av_choice == "2":
            dir_path = input("Enter directory path: ")
            if dir_path:
                result = antivirus_scanner.scan_directory(dir_path)
                print(f"Directory scan complete: {len(result)} files scanned")
        elif av_choice == "3":
            result = antivirus_scanner.update_signatures()
            print(f"Signature update result: {result}")
    elif command == "6":
        print("Password Manager")
        print("(1) Add Password")
        print("(2) Get Password")
        print("(3) Generate Password")
        print("(4) List Services")
        pm_choice = input("Select option: ")
        if pm_choice == "1":
            service = input("Enter service name: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            if service and username and password:
                password_manager.add_password(service, username, password)
                print("Password added successfully")
        elif pm_choice == "2":
            service = input("Enter service name: ")
            username = input("Enter username: ")
            if service and username:
                password = password_manager.get_password(service, username)
                if password:
                    print(f"Password: {password}")
                else:
                    print("Password not found")
        elif pm_choice == "3":
            length = input("Enter password length (default 12): ")
            try:
                length = int(length) if length else 12
            except ValueError:
                length = 12
            password = password_manager.generate_password(length)
            print(f"Generated password: {password}")
        elif pm_choice == "4":
            services = password_manager.list_services()
            print(f"Services: {services}")
    elif command == "7":
        print("Social Engineering Email")
        print("(1) Create Phishing Email")
        print("(2) Analyze Email Content")
        se_choice = input("Select option: ")
        if se_choice == "1":
            to_email = input("Enter recipient email: ")
            subject = input("Enter subject (default: Urgent Security Update): ")
            subject = subject if subject else "Urgent Security Update"
            body = input("Enter email body: ")
            if to_email:
                result = social_engineering_tool.send_test_email(to_email, subject, body)
                print(f"Result: {result}")
        elif se_choice == "2":
            email_content = input("Enter email content to analyze: ")
            if email_content:
                result = social_engineering_tool.analyze_email_content(email_content)
                print(f"Analysis result: {result}")
    elif command == "8":
        print("Goodbye!")
        break
    else:
        print("Invalid command. Please try again.")

