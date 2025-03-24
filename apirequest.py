import requests
import time

API_URL = "http://35.200.185.69:8000/v1/autocomplete?query=test"
HEADERS = {"User-Agent": "RateLimitTester/1.0"}
MAX_REQUESTS = 115  # Based on observations
BASE_WAIT = 5  # Initial wait time
MAX_WAIT = 60  # Max wait time

total_requests = 0  # Counter to track total requests

def fetch_data():
    global total_requests
    wait_time = BASE_WAIT

    while True:
        for _ in range(MAX_REQUESTS):
            response = requests.get(API_URL, headers=HEADERS)
            total_requests += 1  # Increment counter

            if response.status_code == 429:
                print(f"Rate limit reached! Total Requests: {total_requests}. Waiting {wait_time} seconds...")
                time.sleep(wait_time)
                wait_time = min(wait_time * 2, MAX_WAIT)  # Exponential backoff
                break  # Stop sending requests, wait, and retry

        print(f"Total API Requests Made: {total_requests}")

fetch_data()
