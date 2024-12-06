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



from collections import defaultdict, deque

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

def topological_sort(pages, rules):
    graph = defaultdict(list)
    in_degree = {page: 0 for page in pages}
    
    for X, Y in rules:
        if X in pages and Y in pages:
            graph[X].append(Y)
            in_degree[Y] += 1
    
    queue = deque([node for node in pages if in_degree[node] == 0])
    sorted_pages = []
    
    while queue:
        node = queue.popleft()
        sorted_pages.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_pages

def solve(data):
    rules, updates = parse_input(data)
    incorrect_updates = []
    corrected_updates = []

    for update in updates:
        if not is_valid_update(update, rules):
            incorrect_updates.append(update)
            corrected_updates.append(topological_sort(update, rules))

    middle_sum = sum(corrected_update[len(corrected_update) // 2] for corrected_update in corrected_updates)
    return middle_sum

print(solve(data))
