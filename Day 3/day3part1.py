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


# Regex pattern for valid mul(X,Y) instructions
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

# Find all matches of the pattern in the data
matches = re.findall(pattern, data)

results = []
for x, y in matches:
    x, y = int(x), int(y)
    result = x * y
    results.append(result)

# Calculate the total sum of multiplications
total_sum = sum(results)

# Print the results
print(f"Valid multiplications: {results}")
print(f"Total sum: {total_sum}")