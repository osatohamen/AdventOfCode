import requests

# URL to fetch the input data
url = "https://adventofcode.com/2024/day/5/input"

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



def parse_input(data):
    sections = data.strip().split("\n\n")
    rules = [tuple(map(int, line.split("|"))) for line in sections[0].splitlines()]
    updates = [list(map(int, line.split(","))) for line in sections[1].splitlines()]
    return rules, updates

def is_valid_update(update, rules):
    for X, Y in rules:
        if X in update and Y in update:
            if update.index(X) > update.index(Y):
                return False
    return True

def find_middle(update):
    middle_index = len(update) // 2
    return update[middle_index]

def solve_page_ordering(data):
    rules, updates = parse_input(data)
    valid_updates = [update for update in updates if is_valid_update(update, rules)]
    middle_sum = sum(find_middle(update) for update in valid_updates)
    return middle_sum


print(solve_page_ordering(data))