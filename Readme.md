# API Testing Report

## Overview

This document summarizes the findings from testing the autocomplete API across three different versions: v1, v2, and v3. It details the number of API requests made, the unique names retrieved, and the rate limit behavior observed during testing.

## API Requests Summary

| API Version | Total Requests Made | Unique Names Retrieved |
| ----------- | ------------------- | ---------------------- |
| v1          | 5                   | 50                     |
| v2          | 5                   | 60                     |
| v3          | 5                   | 75                     |

## Rate Limit Observations

During extensive testing, the API encountered rate limit restrictions multiple times. Here are the key observations:

- The total API requests made reached **101**, triggering rate limits.
- Additional requests beyond **102, 103, and 104** resulted in waiting times of **5, 10, 20, and 40 seconds**.
- After reaching **116 requests**, the API returned a **429 (Too Many Requests)** error, requiring a 5-second wait before retrying.
- Rate limits were consistent across multiple test queries.

## Query Testing Results

Several test queries were performed to evaluate API response behavior:

### Sample Queries and Responses (v1)

- **Query: `a`**
  - Response: 10 names retrieved (e.g., 'aa', 'aabdknlvkc', 'aabrkcd', etc.)
- **Query: `ab`**
  - Response: 10 names retrieved (e.g., 'ab', 'abagnc', 'abclmm', etc.)
- **Query: `xyz`**
  - Response: No results found.
- **Query: `*`**
  - Response: No results found.

### Prefix-Based Searches

A systematic search using prefixes from **'a' to 'z'** was conducted. The total unique names found across all versions amounted to **260**.

## Conclusion

1. **API Version Comparison**:
   - v3 provided the highest number of unique names (75) per 5 requests.
   - v2 retrieved 60 names, whereas v1 retrieved the least (50).
2. **Rate Limiting Observations**:
   - API rate limits were encountered after approximately **100 requests**.
   - Incremental delays occurred, increasing from **5s to 40s**.
   - After 116 requests, a **429 error** was observed.
3. **Behavioral Insights**:
   - Some queries such as `xyz` and `*` returned no results.
   - Prefix-based searches yielded a total of **260** unique names.

## Future Considerations

- Implementing request throttling to avoid rate limiting.
- Exploring alternative API versions (if available) for higher efficiency.
- Investigating strategies to optimize unique name retrieval per request.

This concludes the API testing and analysis report.
