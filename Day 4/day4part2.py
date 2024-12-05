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

def find_x_mas_occurrences(data):
    # Two versions MAS/SAM
    versions = [['M', 'A', 'S'], ['S', 'A', 'M']]
    
    def is_in_bound(r, c):
        return 0 <= r < len(data) and 0 <= c < len(data[r])
    
    def dfs(r, c, idx, direction, version):
        # Depth-first search
        if not is_in_bound(r, c) or data[r][c] != versions[version][idx]:
            return False
        
        idx += 1
        if idx == 3:
            return True
        
        return dfs(r + direction[0], c + direction[1], idx, direction, version)
    
    answer = 0
    
    # Central 'A'
    for r in range(len(data)):
        for c in range(len(data[r])):
            if data[r][c] == 'A':
                word1 = False
                word2 = False
                
                # Top-left and bottom-right
                if is_in_bound(r-1, c-1):
                    if data[r-1][c-1] == 'M':
                        word1 = dfs(r-1, c-1, 0, (1, 1), 0)
                    elif data[r-1][c-1] == 'S':
                        word1 = dfs(r-1, c-1, 0, (1, 1), 1)
                
                # Top-right and bottom-left 
                if is_in_bound(r-1, c+1):
                    if data[r-1][c+1] == 'M':
                        word2 = dfs(r-1, c+1, 0, (1, -1), 0)
                    elif data[r-1][c+1] == 'S':
                        word2 = dfs(r-1, c+1, 0, (1, -1), 1)
                
                # Count if both diagonals form a valid pattern
                if word1 and word2:
                    answer += 1
    
    return answer


# Print X-MAS occurrences
print(f"XMAS occurs {find_x_mas_occurrences(data)} times")