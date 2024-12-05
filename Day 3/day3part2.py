import requests
import re

# URL to fetch the input data
url = "https://adventofcode.com/2024/day/3/input"

# Session cookie to authenticate the request
session_cookie = "53616c7465645f5f8a41821e31b68e3ef54e27a2a32d25d591ba9c9e31d4f103f73d2109bf527fc5eface3286e96f8ca02cca0a1fa544e0a1960157e46fa3d21"

# Fetch the data
headers = {
    "Cookie": f"session={session_cookie}",
    "User-Agent": "Python script for Advent of Code"
}
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.text.strip()  # Remove any trailing spaces or newline
    print("Data successfully loaded!")
else:
    print(f"Failed to load data: {response.status_code}")


# Regex patterns
mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"


def process_instructions(data):
    results = []
    mul_enabled = True  # Initially enabled
    
    while data:
        # Find occurrences of instruction types
        mul_match = re.search(mul_pattern, data)
        do_match = re.search(do_pattern, data)
        dont_match = re.search(dont_pattern, data)
        
        matches = [
            (mul_match, 'mul') if mul_match else None,
            (do_match, 'do') if do_match else None,
            (dont_match, 'dont') if dont_match else None
        ]
        matches = [m for m in matches if m is not None]
        
        if not matches:
            break
        
        # Sort matches by their position
        matches.sort(key=lambda x: x[0].start())
        earliest_match, match_type = matches[0]
        
        # Multiply based on match type
        if match_type == 'mul':
            if mul_enabled:
                x, y = map(int, earliest_match.groups())
                results.append(x * y)
            data = data.replace(earliest_match.group(0), '', 1)
        elif match_type == 'do':
            mul_enabled = True
            data = data.replace(earliest_match.group(0), '', 1)
        elif match_type == 'dont':
            mul_enabled = False
            data = data.replace(earliest_match.group(0), '', 1)
    
    return results

# Process instructions
results = process_instructions(data)

# Total sum
total_sum = sum(results)

# Print the results
print(f"Valid multiplications: {results}")
print(f"Total sum: {total_sum}")