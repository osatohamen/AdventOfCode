import requests

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


# Sort both lists in ascending order
left_list.sort()
right_list.sort()

# Calculate the differences
differences = [abs(left - right) for left, right in zip(left_list, right_list)]

# Calculate the sum of the differences
answer = sum(differences)

# Print the sorted lists and their differences
print("\nSorted Numbers and Differences:")
print(f"{'Left':>8} | {'Right':>8} | {'Difference':>11}")
print("-" * 33)

for left, right, diff in zip(left_list, right_list, differences):
    print(f"{left:>8} | {right:>8} | {diff:>11}")

# Print the total sum of differences
print("-" * 33)
print(f"{'Total':>19} | {answer:>11}")