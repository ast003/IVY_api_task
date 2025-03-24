import requests
import time

API_URL = "http://35.200.185.69:8000/v1/autocomplete?query=test"
HEADERS = {"User-Agent": "RateLimitTester/1.0"}

def test_rate_limit():
    count = 0
    while True:
        try:
            response = requests.get(API_URL, headers=HEADERS)
            count += 1
            print(f"Request {count}: Status {response.status_code}")

            if response.status_code == 429:  # Too Many Requests
                retry_after = int(response.headers.get("Retry-After", 5))  # Default to 5 seconds if not provided
                print(f"Rate limit reached! Waiting {retry_after} seconds...")
                time.sleep(retry_after)
            elif response.status_code != 200:
                print(f"Unexpected status code: {response.status_code}")
                break

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    test_rate_limit()
