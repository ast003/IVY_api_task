import requests
import time
import string

BASE_URL = "http://35.200.185.69:8000/v1/autocomplete"
HEADERS = {"User-Agent": "API Explorer"}


def test_api(query):
    """Makes an API request with the given query and handles rate limits."""
    url = f"{BASE_URL}?query={query}"
    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 429:
            print("Rate limit exceeded. Retrying after delay...")
            time.sleep(5)  # Adjust the delay as needed
            return test_api(query)
        else:
            print(f"Error {response.status_code}: {response.text}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    return None


def explore_api():
    """Tests the API with predefined queries to observe its behavior."""
    print("Exploring API behavior...")
    test_queries = ["a", "ab", "xyz", "*"]  # Different test cases
    for query in test_queries:
        print(f"Testing query: {query}")
        result = test_api(query)
        print(f"Response: {result}\n")
        time.sleep(1)  # Prevent hitting rate limits


def brute_force_search():
    """Searches the API using single-letter prefixes and collects unique names."""
    found_names = set()

    for letter in string.ascii_lowercase:
        print(f"Searching with prefix: {letter}")
        result = test_api(letter)
        if result and "results" in result:
            found_names.update(result["results"])  # Corrected key from "names" to "results"
        time.sleep(1)  # Prevent excessive requests

    print(f"Total unique names found: {len(found_names)}")
    print(sorted(found_names))  # Print sorted list for better readability
    return found_names


if __name__ == "__main__":
    explore_api()
    names = brute_force_search()
