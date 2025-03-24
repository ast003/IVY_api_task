import requests
import time

BASE_URL = "http://35.200.185.69:8000/v3/autocomplete"  # changed v1 v2 v3 accordingly
QUERY_PARAMS = "query={}"  # Modify as needed
RATE_LIMIT_WAIT = 5  # Initial wait time in seconds after rate limiting

def fetch_autocomplete_results():
    total_requests = 0
    retrieved_names = set()  # Store unique names

    search_terms = ["a", "b", "c", "d", "e"]  # Modify with better search expansion

    for term in search_terms:
        while True:
            response = requests.get(f"{BASE_URL}?{QUERY_PARAMS.format(term)}")
            total_requests += 1  # Increment request count
            print(f"Request {total_requests}: Status {response.status_code}")

            if response.status_code == 200:
                data = response.json()
                retrieved_names.update(data.get("results", []))  # Store unique results
                break  # Move to next term
            
            elif response.status_code == 429:  # Rate limit hit
                print(f"Rate limit reached! Waiting {RATE_LIMIT_WAIT} seconds...")
                time.sleep(RATE_LIMIT_WAIT)
                continue 

            else:
                print(f"Unexpected error: {response.status_code}")
                break  

    print(f"\nTotal API Requests Made for v3: {total_requests}")
    print(f"Total Unique Names Retrieved: {len(retrieved_names)}")

fetch_autocomplete_results()
