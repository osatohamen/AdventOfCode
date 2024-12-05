import requests

# URL to fetch the input data
url = "https://adventofcode.com/2024/day/4/input"

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

data = data.splitlines()

def find_xmas_occurrences(data):
    directions = [
        (0, 1),   # right
        (1, 1),   # down-right
        (1, 0),   # down
        (1, -1),  # down-left
        (0, -1),  # left
        (-1, -1), # up-left
        (-1, 0),  # up
        (-1, 1)   # up-right
    ]
    
    def is_valid(x, y):
        return 0 <= x < len(data) and 0 <= y < len(data[0])
    
    def check_xmas(x, y, dx, dy):
        # Check if XMAS can be formed
        if not is_valid(x + dx*3, y + dy*3):
            return False
        
        xmas_letters = 'XMAS'
        for i in range(4):
            if data[x + i*dx][y + i*dy] != xmas_letters[i]:
                return False
        return True
    
    xmas_positions = set()
    
    # Check every possible starting position
    for x in range(len(data)):
        for y in range(len(data[0])):
            for dx, dy in directions:
                if check_xmas(x, y, dx, dy):
                    occurrence = frozenset(
                        (x + i*dx, y + i*dy) for i in range(4)
                    )
                    xmas_positions.add(occurrence)
    
    return len(xmas_positions)

# Count XMAS occurrences
print(f"XMAS occurs {find_xmas_occurrences(data)} times")