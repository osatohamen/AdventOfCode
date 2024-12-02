import requests
from collections import Counter

# URL to fetch the input data
url = "https://adventofcode.com/2024/day/1/input"

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

# Split the data into lists
left_list = []
right_list = []

# Loop through each line
for line in data.split('\n'):
    # Split the line into two numbers
    numbers = line.split()
    if len(numbers) == 2:  # Ensure there are exactly two numbers
        left_list.append(int(numbers[0]))
        right_list.append(int(numbers[1]))

print("Left list:", left_list)
print("Right list:", right_list)


# Count the occurrences of each number in the right list
right_counts = Counter(right_list)

# Calculate the similarity score
similarity_score = 0
for num in left_list:
    similarity_score += num * right_counts[num]

# Print the similarity score
print(f"\nSimilarity Score: {similarity_score}")