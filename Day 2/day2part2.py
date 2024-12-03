import requests

# URL to fetch the input data
url = "https://adventofcode.com/2024/day/2/input"

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

# 
reports = data.splitlines()


def is_safe(report):
    # Check if a report is safe.
    levels = list(map(int, report.split()))
    differences = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]

    # Check if differences are all positive (increasing) or all negative (decreasing)
    if all(1 <= diff <= 3 for diff in differences) or all(-3 <= diff <= -1 for diff in differences):
        return True
    return False

def can_be_safe(report):
    # Check if removing one level makes the report safe.
    levels = list(map(int, report.split()))
    for i in range(len(levels)):
        # Create a new report with the i-th level removed
        modified_report = levels[:i] + levels[i + 1:]
        if is_safe(" ".join(map(str, modified_report))):
            return True
    return False

# Count safe reports
safe_reports = 0
for report in reports:
    if is_safe(report) or can_be_safe(report):
        safe_reports += 1

print(f"Number of safe reports: {safe_reports}")